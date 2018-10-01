#!/usr/bin/python

"""
Saving the Universe problem solution
(GCJ 2008, Qualification Round)
Author: madrezaan
"""

import sys

# open input file
if len(sys.argv) == 2 and sys.argv[1] != '--help':
    in_file = open(sys.argv[1])
else:
    print "Usage: saving_the_universe.py <input file>"
    sys.exit(0)

# get number of cases
num_cases = int(in_file.readline())

# begin prosessing cases
for cur_case in range(num_cases):

    # get names of engines
    engines_names = []
    num_engines = int(in_file.readline())
    for i in range(num_engines):
        engines_names.append(in_file.readline())
        
    # scan queries
    num_switches = 0
    strict_engines = map(lambda(x): False, range(num_engines))
    num_queries = int(in_file.readline())
    num_strict = 0
    for i in range(num_queries):
        cur_query = in_file.readline()
        for j in range(num_engines):
            if cur_query == engines_names[j] and not strict_engines[j]:
                num_strict += 1
                if num_strict == num_engines:
                    num_strict = 1
                    num_switches += 1
                    strict_engines = map(lambda(x): False, range(num_engines))
                strict_engines[j] = True
                break

    # print result
    print "Case #%d: %d" % (cur_case + 1, num_switches)
                
in_file.close()


