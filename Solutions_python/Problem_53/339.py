#!/usr/bin/python

"""
Snapper Chain problem solution
(GCJ 2010, Qualification Round)
Author: madrezaan
"""

import sys, math

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: snapper_chain.py <input file>"
    sys.exit(0)

# get number of cases
T = int(in_file.readline())

# begin prosessing cases
for cur_case in range(T):
    # get constants
    N, K = map(int, in_file.readline().split(" "))
    # calculate light state after K snaps
    is_light = ["OFF", "ON"][(K + 1) % int(math.pow(2, N)) == 0]
    # output result
    print "Case #%d: %s" % (cur_case + 1, is_light)

# close input file
in_file.close()

    
        
