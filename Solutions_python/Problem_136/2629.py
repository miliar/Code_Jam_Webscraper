#-*- coding: utf-8 -*-

import sys

_in = sys.stdin

def solve():
    line = [float(x) for x in _in.readline().split(" ")]
    C = line[0] # valor da farm
    F = line[1] # fator incremental
    X = line[2] # quero esse valor aqui ;)

    Fi = 2
    seconds = 0

    while 1:
        ot = seconds + X / Fi
        on = seconds + C / Fi + X / (Fi + F)
        if on >= ot:
            seconds = ot
            break
        else:
            seconds = seconds + C / Fi
            Fi += F

    return seconds

T = int(_in.readline())
Ti = 1

while Ti <= T:
    print "Case #%d: %0.07lf" % (Ti, solve())
    Ti += 1


