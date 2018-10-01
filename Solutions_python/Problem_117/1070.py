#!/usr/bin/env python2
# coding: utf-8

from itertools import islice
import sys

T = int(sys.stdin.readline())


for case in range(1,T+1):
    N, M = map(int, sys.stdin.readline().split())
    rowmax = [0] * N
    colmax = [0] * M
    field = []
    for i in range(N):
        field.append(map(int, sys.stdin.readline().split()))
        for j, height in enumerate(field[-1]):
            rowmax[i] = max(rowmax[i], height)
            colmax[j] = max(colmax[j], height)

    ans = 'YES'
    for i, row in enumerate(field):
        for j, height in enumerate(row):
            if height != rowmax[i] and height != colmax[j]:
                ans = 'NO'

    print 'Case #%d: %s' % (case, ans)
