#!/usr/bin/env python

import sys

ls = sys.stdin.readlines()[1:]
C = 1
for l in ls:
    a, b = l.split(" ")
    a = [c for c in a]
    k = int(b)
    n = 0

    def flip(i):
        for j in range(i, i + k):
            a[j] = '-' if a[j] == '+' else '+'
    
    for i in range(len(a) - k + 1):
        if a[i] == '-':
            flip(i)
            n += 1
    print "Case #%d:" % C,
    C += 1
    if '-' in set(a[len(a) - k + 1:]):
        print "IMPOSSIBLE"
    else:
        print n

