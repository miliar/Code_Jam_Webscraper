#!/usr/bin/python2
# coding: utf-8

import itertools
from sys import stdin

T = int(stdin.readline().rstrip())

for ct in range(T):
    fans = int(stdin.readline().rstrip()) - 1

    for lnum in range(4):
        line = stdin.readline()
        if lnum == fans:
            fcards = set(map(int, line.rstrip().split()))

    sans = int(stdin.readline().rstrip()) - 1

    for lnum in range(4):
        line = stdin.readline()
        if lnum == sans:
            scards = set(map(int, line.rstrip().split()))

    res = fcards & scards

    if not res:
        ans = 'Volunteer cheated!'
    elif len(res) > 1:
        ans = 'Bad magician!'
    else:
        ans = res.pop()

    print 'Case #{0}: {1}'.format(ct + 1, ans)
