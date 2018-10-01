#!/usr/bin/python

"""
Theme Park problem solution
(GCJ 2010, Qualification Round)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: theme_park.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())
# begin prosessing cases
for cur_case in range(T):
    # get constants
    R, k, N = map(int, in_file.readline().split(" "))
    g = map(int, in_file.readline().split(" "))
    # start modelling
    total = 0
    ride = 0
    invariant = []
    cur_step = 0
    while ride < R:
        # single ride step
        count = 0
        for i in range(N + 1):
            if i < N and count + g[i] <= k:
                count += g[i]
            else:
                break
        g = g[i:] + g[:i]
        cur_step = (cur_step + i) % N
        # invariant detection
        try:
            start_step = invariant.index((cur_step, count))
            invariant = invariant[start_step:]
            break
        except ValueError:
            invariant.append((cur_step, count))
        total += count
        ride += 1
    # calculate rest steps of invariant
    if ride < R:
        steps_left = R - ride
        if steps_left >= len(invariant):
            total += (steps_left // len(invariant)) * sum(map(lambda x: x[1], invariant))
        steps_left = steps_left % len(invariant)
        total += sum(map(lambda x: x[1], invariant[:steps_left]))
    # output result
    print "Case #%d: %d" % (cur_case + 1, total)

# close input file
in_file.close()

    
        
