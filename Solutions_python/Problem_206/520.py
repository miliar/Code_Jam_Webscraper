#!/usr/bin/env python3
# -*- coding: utf-8 -*-


T = int(input())  # number of test cases
for t in range(T):
    D, N = [int(v) for v in input().split()]  # destination and horses
    KS = list()
    for n in range(N):
        k, s = [int(v) for v in input().split()]  # position and speed
        KS.append([k, s])

    # solve
    # only the one that takes more time matters
    maxtim = 0
    for k, s in KS:
        tim = (D - k) / s
        if tim > maxtim:
            maxtim = tim
    maxvel = D / maxtim

    print("Case #{:d}: {:.6f}".format(t + 1, maxvel))
