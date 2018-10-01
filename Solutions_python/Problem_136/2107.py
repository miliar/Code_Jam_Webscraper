#!/usr/bin/env python

f = open('B-large.in')

T = int(f.readline())

for i in range(1, T+1):
    init = f.readline().split()
    C = float(init[0])
    F = float(init[1])
    X = float(init[2])
    P = 2.0
    time = 0
    while C/P + X/(F+P) < X/P:
        time += C/P
        P += F
    time += X/P
    print "Case #{0}: {1}".format(i, time)
