#!/usr/bin/env python
import sys
import math

cases = []
with open(sys.argv[1]) as f:
    casecount = int(f.readline())
    for _ in xrange(0, casecount):
        x, r, c = map(int, f.readline().split(" "))

        cases.append((x, r, c))

caseno = 1
for x, r, c in cases:
    biggest_square = (int(math.ceil((x-1)/2.0))+1, ((x-1)/2)+1)

    if r*c < x:
        winner = "RICHARD"
        reason = "Area too small"
    elif (r*c) % x != 0:
        winner = "RICHARD"
        reason = "Area not divisible"
    elif r < x and c < x:
        winner = "RICHARD"
        reason = "Area too small for straight omino"
    elif ((r < biggest_square[0] or c < biggest_square[1])
        and (c < biggest_square[0] or r < biggest_square[1])):
        winner = "RICHARD"
        reason = "Area too small for square omino"
    elif x>=4 and (x >= 2*r-1 or x >= 2*c-1):
        winner = "RICHARD"
        reason = "Area too small for zigzag omino"
    else:
        winner = "GABRIEL"
        reason = ""

    print "Case #%s: %s" % (caseno, winner)
    caseno += 1
