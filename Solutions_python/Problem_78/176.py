#!/usr/bin/python

import sys
from fractions import Fraction

EXAMPLE = 0

def solve(case):
    N, Pd, Pg = case
    if Pd == 0 and Pg == 0:
        return "Possible"
    if Pd == 100 and Pg == 100:
        return "Possible"
    if Pg == 0 or Pg == 100:
        return "Broken"
    if N < Fraction(Pd, 100).denominator:
        return "Broken"
    return "Possible"


def main(data = "A-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    T = int(inp[0])
    inp.pop(0)
    j = 1
    for case in inp:
        print "Case #" + str(j) + ": " + str(solve(map(int, case.split())))
        j += 1


if EXAMPLE:
    main()
else:
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print sys.argv[0] + " <input file>"
