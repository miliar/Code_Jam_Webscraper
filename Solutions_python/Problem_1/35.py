# Saving the Universe
#
# Usage: python saving.py test.in

import pdb

def read_case(fp):
    """Returns (engines, queries).
    """

    s = int(fp.readline().strip())
    engines = []
    for i in range(s):
        engines.append(fp.readline().strip())

    q = int(fp.readline().strip())
    queries = []
    for i in range(q):
        queries.append(fp.readline().strip())

    return (engines, queries)

def min_switches(engines, queries):
    if len(queries) == 0:
        return 0

    cost = {}

    for e in engines:
        if e == queries[0]:
            cost[(e, 0)] = float('inf')
        else:
            cost[(e, 0)] = 0

    for k in range(1, len(queries)):
        for e in engines:
            if e == queries[k]:
                cost[(e, k)] = float('inf')
            else:
                a = [cost[(f, k-1)] + 1 for f in engines if f != e]
                a.append(cost[(e, k-1)])
                cost[(e, k)] = min(a)
    q = len(queries) - 1
    return min(cost[(e, q)] for e in engines)

import sys

input = open(sys.argv[1])

n = int(input.readline().strip())
for i in range(n):
    (engines, queries) = read_case(input)
    print "Case #%d: %d" % (i+1, min_switches(engines, queries))
