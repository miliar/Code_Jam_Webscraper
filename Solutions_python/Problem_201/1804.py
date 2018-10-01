from math import floor, ceil
from heapq import *

def go(N, K):
    # if K == 1:
        # return max(ceil((N - 1) / 2), 0), max(floor((N - 1) / 2), 0)
    q = []
    heappush(q, -N)
    for _ in range(K):
        a = -heappop(q)
        l, r = max(a / 2, 0), max((a - 1) / 2, 0)
        heappush(q, -l)
        heappush(q, -r)
    return max(l, r), min(l, r)


for q in range(1, input() + 1):
    N, K = map(int, raw_input().split())
    print "Case #%s: %s %s" % ((q,) + tuple(map(int, go(N, K))))
