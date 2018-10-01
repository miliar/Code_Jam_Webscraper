#!/usr/bin/env python3

import math
import sys
import operator

from functools import reduce

def solve(N, K, U, P):
    # yay hardcoding
    assert N == K
    P.sort()

    while U > 0.0:
        v = P[0]
        c = 0
        while c < N and P[c] == v:
            c += 1
        target = P[c] if c < N else 1.0
        offset = target - v
        if offset == 0.0:
            break
        to_add = min(offset * c, U)
        if to_add == U:
            for i in range(c):
                P[i] += to_add / c
            break
        else:  # to_add == offset * c
            U -= to_add
            for i in range(c):
                P[i] = target
        #print(P, file=sys.stderr)

    return reduce(operator.mul, P, 1)


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    U = float(input())
    P = list(map(float, input().split()))

    res = solve(N, K, U, P)
    print('Case #{}: {}'.format(t+1, res))

