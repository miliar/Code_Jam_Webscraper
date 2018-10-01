from __future__ import division
from sys import stdin, stdout
import heapq
import math

def solve(N, K):
    spaces = []
    heapq.heappush(spaces, -N)

    for _ in xrange(K):
        size = -heapq.heappop(spaces)

        half_size = (size - 1) / 2
        ceil = math.ceil(half_size)
        floor = math.floor(half_size)
        if ceil > 0:
            heapq.heappush(spaces, -ceil)

            if floor > 0:
                heapq.heappush(spaces, -floor)

    return "{} {}".format(int(ceil), int(floor))
    

T = int(stdin.readline())

for t in range(T):
    N, K = map(int, stdin.readline().strip().split())

    result = solve(N, K)

    stdout.write("Case #%d: %s\n"%(t+1, result))