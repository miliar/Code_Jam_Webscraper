#!/usr/local/bin/pypy
# run with PyPy 2.6.1

import heapq

def read_strings():
    return raw_input().strip().split(' ')

def read_ints():
    return [int(x) for x in read_strings()]

def solve(n, k):
    heap = []
    heapq.heappush(heap, -n)
    for i in xrange(k):
        nlength = heapq.heappop(heap)
        ls = (-nlength - 1) / 2
        rs = (-nlength) / 2
        heapq.heappush(heap, -ls)
        heapq.heappush(heap, -rs)
    return max(ls, rs), min(ls, rs)

test_count, = read_ints()
for test in xrange(1, test_count + 1):
    n, k = read_ints()
    y, z = solve(n, k)
    print 'Case #{}: {} {}'.format(test, y, z)
