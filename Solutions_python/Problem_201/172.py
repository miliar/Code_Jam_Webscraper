#!/usr/bin/env python3

import sys
from heapq import heappush, heappop

def solve(N, K):
    pq = []  # largest sz -> mult by -1
    heappush(pq, (-N, 1))

    while K > 0:
        sz, count = heappop(pq)
        while pq and pq[0][0] == sz:
            count += heappop(pq)[1]

        sz *= -1
        K -= count
        mid = (sz - 1) // 2
        #print('popped', sz, count)

        # left partition
        left_sz = mid
        if left_sz > 0:
            heappush(pq, (-left_sz, count))
            #print('push left', left_sz)

        # right partition
        right_sz = sz - mid - 1
        if right_sz > 0:
            heappush(pq, (-right_sz, count))
            #print('push right', right_sz)

    return '{} {}'.format(sz - mid - 1, mid)

T = int(input())
for t in range(T):
    a, b = input().split()
    res = solve(int(a), int(b))
    print('Case #{}: {}'.format(t+1, res))
    #print('Case #{}: {}'.format(t+1, res), file=sys.stderr)

