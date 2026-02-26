#!/usr/bin/python

# Ensure invalid standalone ':' token does not loop forever.

from keystone import *

import regress


class TestX64StandaloneColon(regress.RegressTest):
    def runTest(self):
        ks = Ks(KS_ARCH_X86, KS_MODE_64)

        with self.assertRaises(KsError) as ctx:
            ks.asm(b":", 0x1000)

        self.assertEqual(ctx.exception.errno, KS_ERR_ASM_STAT_TOKEN)


if __name__ == '__main__':
    regress.main()
