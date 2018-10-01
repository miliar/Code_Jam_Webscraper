#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem A. Consonants
# https://code.google.com/codejam/contest/2437488/dashboard#s=p0
#

import sys
import re


def solve(name, n):
    result = 0#set()
    for start in range(len(name) - n + 1):
        for l in range(n, len(name) - start + 1):
            newname = name[start:][:l]
            if re.search('([^aiueo]){%d}' % n, newname):
                #result.add(newname)
                result += 1
    return result#len(result)


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        name, n = IN.readline().split()
        OUT.write('Case #%d: %d\n' % (index + 1, solve(name, int(n))))


def makesample(Lmax=100, T=100):
    import random
    import string
    print T
    for index in range(T):
        L = random.randint(1, Lmax)
        n = random.randint(1, L)
        print ''.join([random.choice(string.lowercase) for n in range(L)]), n


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

