from copy import copy
from itertools import combinations
from math import log
from operator import xor
import time

def solve(values):
    N = len(values)
    values.sort()
    for i in xrange(1, N):
        xor_sean = reduce(xor, values[i:])
        xor_patrick = reduce(xor, values[:i])
        if xor_sean == xor_patrick:
            return sum(values[i:])

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        N = int(raw_input())
        values = [int(v) for v in raw_input().split()]
        assert(len(values) == N)
        r = solve(values)
        print 'Case #%d: %s' % (i, 'NO' if r is None else str(r))
