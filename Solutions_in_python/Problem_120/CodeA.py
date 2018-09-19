#! /usr/bin/env python
import sys
import math
from decimal import Decimal
import bisect
import itertools

sample = "sample"

if len(sys.argv) < 2:
    print "usage: %s [sample | name]" % (sys.argv[0], )
    sys.exit(1)

if sys.argv[1].lower() == "sample":
    fin = open(sample + ".in", "r") 
    fout = open(sample + ".out", "w")
else:
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[1] + ".out", "w")

case = 1
ncases = int(fin.readline())

def solve(r, t):
    temp = 4 * (r ** 2) - 4 * r + 8 * t + 1
    temp = Decimal(temp).sqrt()
    n = 1/ Decimal(4) * (temp - 2 * r + 1)
    return n

while True:
    line = fin.readline()
    line = line.rstrip()

    parts = line.split()
    r = long(parts[0])
    t = long(parts[1])

    soln = solve(r, t)
    soln = int(math.floor(soln))

    msg = "Case #%d: %d\n" % (case, soln)
    fout.write(msg)
    case += 1

    if case > ncases:
        break

fin.close()
fout.close()
