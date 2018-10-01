#!/opt/local/bin/python

"""Premature optimization is the root of all evil."""

import sys
import re

def doit(D, N):
    t = 0

    for _ in range(N):
        (k, s) = [int(x) for x in sys.stdin.readline().split()]
        if k >= D:
            continue
        l = (D-k) / s
        if l > t:
            t = l

    return D / t

T = int(sys.stdin.readline())
for casenum in range(T):
    data = [int(x) for x in sys.stdin.readline().split()]

    n = str(doit(*data))




    print("Case #" + str(casenum + 1) + ": " + n)
