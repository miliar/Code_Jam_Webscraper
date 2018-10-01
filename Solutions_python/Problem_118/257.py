#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Problem C. Fair and Square
# https://code.google.com/codejam/contest/2270488/dashboard#s=p2
#

import sys
import math
import itertools


class Palindromes(list):
    PALINDROMES_FILE = 'palindromes.txt'

    def __init__(self):
        import os
        if not os.path.isfile(self.PALINDROMES_FILE):
            self.maketarget(10**14)
        self[:] = map(int, open(self.PALINDROMES_FILE).read().split())

    @classmethod
    def maketarget(cls, nmax):
        with open(cls.PALINDROMES_FILE, 'w') as f:
            for n in cls.itertarget():
                if n > nmax:
                    break
                f.write(str(n) + ' ')
                print n

    @classmethod
    def itertarget(cls):
        return (n for n in cls.iterpalindrome() if cls.ispalindrome(n ** 2))

    @classmethod
    def iterpalindrome(cls):
        for l in itertools.count(1):
            for p in itertools.product('0123456789', repeat=(l + 1) / 2):
                if p[0] == '0':
                    continue
                yield int(''.join(p[:-1] + p[::-1]) if (l % 2) else ''.join(p + p[::-1]))

    @classmethod
    def ispalindrome(cls, n):
        return str(n) == str(n)[::-1]

palindromes = tuple(Palindromes())


def solve(A, B):
    solution = []
    start = int(math.sqrt(A))
    end = int(math.sqrt(B))
    for n in palindromes:
        if start <= n <= end and A <= n ** 2 <= B:
            solution.append(n)
    return len(solution)


def main(IN, OUT):
    T = int(IN.readline())
    for index in range(T):
        A, B = map(int, IN.readline().split())
        OUT.write('Case #%d: %s\n' % (index + 1, solve(A, B)))


def makesample(T=10000, ABmax=10**14):
    import random
    print T
    for index in range(T):
        A = random.randint(1, ABmax)
        B = random.randint(A, ABmax)
        print A, B


if __name__ == '__main__':
    if '-makesample' in sys.argv[1:]:
        makesample()
    else:
        main(sys.stdin, sys.stdout)

