#!/usr/bin/python -u

import sys
import os
from sys import stdin

T = int(stdin.readline())

for o in range(1, T + 1):
    IN = stdin.readline().strip().split(' ')
    C = float(IN[0])
    F = float(IN[1])
    X = float(IN[2])

    cookie = 0.0
    farm = 0.0
    S = 0.0
    prevBS = 999999.999999

    for BUYFARM in range(0, 100000):
        cps = 2.0 + (F * farm)

        # no buy, waiting nS seconds to end
        nS = S + (X - cookie) / cps

        # buy, waiting n seconds
        bS = S + (C - cookie) / cps
        S = bS
        cookie = 0.0
        farm = farm + 1
        cps = 2.0 + (F * farm)
        # after buy, waiting p seconds to end
        bS = bS + (X - cookie) / cps

        if nS < bS:
            S = nS
            break; # STOP

        if prevBS < bS:
            S = prevBS
            break; # STOP

        prevBS = bS

    print 'Case #%d: %.7f' % (o, S)



