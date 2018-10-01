# GCJ 2014 Qualification, problem B, Jeremy Holman

import sys

T = int(sys.stdin.readline().strip())

for i in xrange(T):
    C, F, X = map(float, sys.stdin.readline().strip().split(" "))

    candidate = float('inf')
    income = 2.0
    time = 0.0
    new_candidate = X / income

    while new_candidate < candidate:
        candidate = new_candidate
        time += C / income
        income += F
        new_candidate = time + X/income

    print "Case #%d: %.7f" % (i+1, candidate)
