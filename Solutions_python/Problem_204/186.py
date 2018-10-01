#!/opt/local/bin/python

"""Premature optimization is the root of all evil."""

import sys
import re

from math import ceil, floor

def isaset(nums, R):
    minx = ceil(10*nums[0]/(11*R[0]))
    manx = floor(10*nums[0]/(9*R[0]))
    for i in range(1, len(R)):
        r = [ceil(10*nums[i]/(11*R[i])), floor(10*nums[i]/(9*R[i]))]
        minx = min(minx, r[0])
        manx = max(manx, r[1])
    return minx <= manx


def doit(N, P, R, amts):
    """Well, lets get the small case at least..."""

    srs = [0 for _ in R]
    for i in range(len(R)):
        srs[i] = [(ceil(10*a/(11*R[i])), floor(10*a/(9*R[i]))) for a in amts[i]]

    sets = 0
    usd = [0 for _ in R]
    while usd[0] < len(srs[0]):
        good = True
        r = srs[0][usd[0]]
        if r[1] < r[0]:
            usd[0] += 1
            continue
        t = usd[:]
        for I in range(1,len(R)):
            t[I] = usd[I]
            while srs[I][t[I]][1] < r[0]:
                t[I] += 1
                if t[I] >= len(srs[I]):
                    good = False
                    break
            if good and srs[I][t[I]][0] > r[1]:
                good = False
                usd[I] = t[I]
            if not good:
                break
        if good:
            usd[1:] = [x + 1 for x in t[1:]]
            sets += 1
        usd[0] += 1

    return sets

        

T = int(sys.stdin.readline())
for casenum in range(T):
    data = [int(x) for x in sys.stdin.readline().split()]
    rec = [int(z) for z in sys.stdin.readline().split()]
    amts = []
    for i in range(data[0]):
        amts.append(sorted([int(y) for y in sys.stdin.readline().split()]))
    n = doit(data[0], data[1], rec, amts)




    print("Case #" + str(casenum + 1) + ": " + str(n))
