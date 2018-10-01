#!/usr/bin/python2
# coding: utf-8

import itertools
from sys import stdin

T = int(stdin.readline().rstrip())

for ct in range(T):
    _, counts = stdin.readline().split()

    ans = 0
    d = 0
    for curr in counts:
        d += int(curr) - 1
        if d < 0:
            ans -= d
            d = 0

    print 'Case #{0}: {1}'.format(ct + 1, ans)
