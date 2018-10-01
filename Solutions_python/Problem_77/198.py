#!/usr/bin/env python

t = int(raw_input())

def solve(array):
    seen = set()
    cycle_lengths = []
    for i in xrange(len(array)):
        if i != array[i] - 1 and i not in seen:
            seen.add(i)
            j = array[i] - 1
            l = 1
            while j != i:
                l += 1
                seen.add(j)
                j = array[j] - 1
            cycle_lengths.append(l)
    return sum(cycle_lengths)

for tc in xrange(1, t+1):
    n = int(raw_input())
    array = map(int, raw_input().split())
    print("Case #%d: %.6f" % (tc, solve(array)))
