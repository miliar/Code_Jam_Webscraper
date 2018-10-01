#!/usr/bin/python3

import sys
from heapq import *

def solve(n, k):
    h = []
    d = {}
    d[n] = 1
    heappush(h, -n)
    while True:
        l = -heappop(h)
        a, b = (l - 1) // 2, (l - 1) // 2
        if l % 2 == 0:
            a += 1
        # print(l, k, d[l])
        if k <= d[l]:
            return a, b
        k -= d[l]
        if a not in d:
            heappush(h, -a)
        d[a] = d.get(a, 0) + d[l]
        if b not in d:
            heappush(h, -b)
        d[b] = d.get(b, 0) + d[l]
        
t = int(sys.stdin.readline())

for i in range(1, t+1):
    n, k = map(int, sys.stdin.readline().split())
    a, b = solve(n, k)
    print('Case #{0}: {1} {2}'.format(i, a, b))
