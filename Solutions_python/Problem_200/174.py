#!/usr/bin/env python
from __future__ import print_function

import sys

INPUT_FILE = "b2.in"
OUTPUT_FILE = "b2.out"


def log(message):
    print(message, file=sys.stderr)

with open(INPUT_FILE, 'r') as fin, open(OUTPUT_FILE, 'w') as fout:
    sys.stdout = fout

    T = int(fin.readline())
    for tc in range(T):
        log('Test Case %d' % (tc+1))

        N = list(fin.readline().strip())
        for i in reversed(range(len(N))):
            if i > 0 and ord(N[i]) < ord(N[i-1]):
                for j in range(len(N)-i):
                    N[i+j] = '9'
                j = i-1
                while N[j] == '0':
                    N[j] = '9'
                    j -= 1
                N[j] = chr(ord(N[j])-1)

        print('Case #%d: %s' % (tc+1, int(''.join(N))))
