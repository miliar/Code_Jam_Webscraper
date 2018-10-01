#!/usr/bin/env python

import sys

def isOn(line):
    [N, K] = [int(x) for x in line.split(' ')]
    prefix = (1 << N) - 1
    return ((K & prefix) == prefix)
    

nCases = int(sys.stdin.readline())
case = 0

for line in sys.stdin.readlines():
    case += 1
    if case > nCases:
        break;
    
    state = 'OFF'
    if isOn(line):
        state = 'ON'
    print 'Case #%d: %s' % (case, state)