#!/usr/bin/env python

import math


def pick(areas, K, R):
    if K == 0:
        return 0.0
    res = []
    flag = True
    for a, r in areas:
        if r <= R:
            if r == R and flag:
                flag = False
                continue
            res.append(a)
            if len(res) == K:
                return sum(res)


def solve(N, K, pancakes):
    pancakes = sorted(pancakes, reverse=True)
    areas = [(2*math.pi*r*h, r) for r, h in pancakes]
    areas = sorted(areas, reverse=True)
    return max(
        math.pi*pancakes[i][0]**2 + 2*math.pi*pancakes[i][0]*pancakes[i][1] + pick(areas, K - 1, pancakes[i][0])
        for i in range(N-K+1)
    )


T = int(raw_input().strip())
for t in range(T):
    N, K = [int(x) for x in raw_input().strip().split()]
    pancakes = []
    for n in range(N):
        R, H = [int(x) for x in raw_input().strip().split()]
        pancakes.append((R, H))
    print 'Case #%d: %f' % (t+1, solve(N, K, pancakes))
