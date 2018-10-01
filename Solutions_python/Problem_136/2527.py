#!/usr/bin/python

import sys
from math import *

def Nf(): return tuple(map(float, sys.stdin.readline().split()))
def Ni(): return tuple(map(int, sys.stdin.readline().split()))

T = Ni()[0]
for t in range(1, T + 1):
    C, F, X = Nf()
    rate = 2
    time = 0
    while True:
        timenobuy = X / rate

        timewithbuy = C / rate + X / (rate + F)
        if timenobuy < timewithbuy:
            time += timenobuy
            break
        else:
            time += C / rate
            rate += F

    print "Case #%d: %.7f" % (t, time)

