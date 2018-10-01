#! /usr/bin/env python2.7
import sys,math
from Queue import PriorityQueue
from collections import defaultdict

def solve_small(S, N, K):
    stall_queue = PriorityQueue()
    stall_queue.put((-N, int(N)))
    for i in xrange(K):
        #print (N,K,i)
        n = stall_queue.get()[1] - 1
        n1 = int(math.floor(n/2))
        n2 = int(n - n1)
        if n1 > 0:
            stall_queue.put((-n1, n1))
        stall_queue.put((-n2, n2))

    return (n2, n1)


input_lines = sys.stdin.readlines()
for i, l in enumerate(input_lines):
    if i == 0:  # input case count
        continue
    N, K = map(lambda x: int(x), l.split())
    S = defaultdict(dict)
    ans = solve_small(S, N, K)

    print ('Case #{}: {} {}'.format(i, int(ans[0]), int(ans[1])))
