#!/usr/bin/python -u

import sys
import os
from sys import stdin

T = int(stdin.readline())

for C in range(1, T + 1):
    S1 = [[], [], [], []]
    S2 = [[], [], [], []]

    A1 = int(stdin.readline()) - 1
    for ro in range(0, 4):
        x = stdin.readline().strip().split(' ')
        S1[ro].append(x[0])
        S1[ro].append(x[1])
        S1[ro].append(x[2])
        S1[ro].append(x[3])

    A2 = int(stdin.readline()) - 1
    for ro in range(0, 4):
        x = stdin.readline().strip().split(' ')
        S2[ro].append(x[0])
        S2[ro].append(x[1])
        S2[ro].append(x[2])
        S2[ro].append(x[3])

    X = [x for x in S1[A1] if x in S2[A2]]
    if len(X) > 1: R = 'Bad magician!'
    elif len(X) == 0: R = 'Volunteer cheated!'
    else:
        R = str(X[0])

    print 'Case #%d: %s' % (C, R)
