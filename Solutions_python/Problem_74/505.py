#!/usr/bin/env python
from __future__ import print_function
from itertools import *

ORANGE = 0
BLUE = 1

def read_case():
    tokens = raw_input().split()
    sched = []
    for i in xrange(1, len(tokens), 2):
        sched.append((ORANGE if tokens[i] == 'O' else BLUE, int(tokens[i+1])))
    return sched

def solve(case):
    prev = [(0, 1), (0, 1)]
    time = 0
    for step in case:
        prevtime, prevpos = prev[step[0]]
        other_prevtime = prev[1 - step[0]][0]
        time = max(prevtime + abs(step[1] - prevpos) + 1, other_prevtime + 1)
        prev[step[0]] = (time, step[1])
    return time

T = int(raw_input())
for casenum in xrange(1, T+1):
    print("Case #{}: {}".format(casenum, solve(read_case())))

