#!/usr/bin/env python

import sys
from itertools import combinations, izip
from collections import Counter, defaultdict
from math import sqrt

t = int(sys.stdin.readline())
for testcase in xrange(t):

    [name, n] = sys.stdin.readline().split()
    n = int(n)
    a = b = result = lasta = 0
    while a < len(name):
        if name[a] in 'aeiou':
            a += 1
        else:
            b = a
            while b < len(name) and name[b] not in 'aeiou' and b - a + 1 < n:
                b += 1
            if b == len(name) or name[b] in 'aeiou':
                b -= 1
            if b - a + 1 >= n:
                result += (a+1-lasta) * (len(name) - b)
                # add number of ways substring can be split
                #   result += max(0,sum(xrange((b-a-n+3))))
                lasta = a + 1
            a += 1

    print 'Case #'+str(testcase+1)+':',result
