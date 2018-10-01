#!/usr/bin/env python

from decimal import Decimal
import sys

inp = sys.stdin.read().split('\n')

cases = [(Decimal(case.split()[0]), Decimal(case.split()[1]), Decimal(case.split()[2])) for case in inp[1:] if case]

for case_num, case in enumerate(cases, 1):
    C = case[0]
    F = case[1]
    X = case[2]
    
    def time_to_c(C, F, num_farms):
        return C / (F * num_farms + 2)
    
    t = 0
    num_farms = 0
    while True:
        if time_to_c(X, F, num_farms) < time_to_c(C, F, num_farms) + time_to_c(X, F, num_farms + 1):
            t += time_to_c(X, F, num_farms)
            break
        else:
            t += time_to_c(C, F, num_farms)
            num_farms += 1
    print "Case #%d: %.7f" % (case_num, t)
