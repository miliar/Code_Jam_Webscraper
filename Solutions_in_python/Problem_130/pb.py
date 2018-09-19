#! /usr/bin/env python

from math import log, floor

T = int(input())
for TT in range(1, T + 1):
    n, p = [int(x) for x in input().split()]
    notp = 2 ** n - p
    if notp != 0:
        gu = n - floor(log(notp, 2))
        gu = 2 ** gu - 2
        po =  n - floor(log(p, 2))
        po = 2 ** n - 2 ** po
    else:
        gu = 2 ** n - 1
        po = gu
    print("Case #" + str(TT) + ": " + str(gu) + " " + str(po))
