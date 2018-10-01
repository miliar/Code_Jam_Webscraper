#!/usr/bin/python2 -u
# -*- coding: utf-8 -*-
#
import sys, math

### ----- Variables
LINES = []

### ----- Functions
def pop_line():
    global LINES
    if len(LINES) == 0:
        return None
    line = LINES[0]
    LINES = LINES[1:]
    return line

### ----- Program Main
LINES = [line.rstrip() for line in sys.stdin]

T = int(pop_line())
for t in range(T):

    answer1 = int(pop_line())
    arrange1 = []
    arrange1.append(map(int, pop_line().split()))
    arrange1.append(map(int, pop_line().split()))
    arrange1.append(map(int, pop_line().split()))
    arrange1.append(map(int, pop_line().split()))

    answer2 = int(pop_line())
    arrange2 = []
    arrange2.append(map(int, pop_line().split()))
    arrange2.append(map(int, pop_line().split()))
    arrange2.append(map(int, pop_line().split()))
    arrange2.append(map(int, pop_line().split()))

    candidates = []
    for c in arrange1[answer1-1]:
        if c in arrange2[answer2-1]:
            candidates.append(c)

    if len(candidates) == 0:
        print 'Case #%d: %s' % (t+1, 'Volunteer cheated!')
    elif len(candidates) > 1:
        print 'Case #%d: %s' % (t+1, 'Bad magician!')
    else:
        print 'Case #%d: %d' % (t+1, candidates[0])
