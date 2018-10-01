__author__ = 'bszikszai'

from io import *
from sortedcontainers import SortedList
import math

def simulate(n, k):
    s = SortedList()
    s.add(n)
    for _ in xrange(k):
        st = (s[-1] - 1) / 2.0
        del s[-1]
        maxVal = int(math.ceil(st))
        minVal = int(math.floor(st))
        s.add(minVal)
        s.add(maxVal)
    return "%s %s" % (maxVal, minVal)

def solve(f):
    inp = [int(c) for c in f.readline().rstrip('\n\r ').split()]
    return simulate(inp[0], inp[1])

with open('17/1/C/input.txt', 'r') as f:
    with open('17/1/C/output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))