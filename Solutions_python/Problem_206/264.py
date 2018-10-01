
import os
import sys
import glob
import subprocess
import random
import fileinput


next_line = 0
lines = [line.strip() for line in fileinput.input()]
def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]

def ok(s, D, N, T):
    t = D / s
    for t1 in T:
        if t1 > t:
            return False
    return True


def calc():
    parts = get_line().split()
    D = int(parts[0])
    N = int(parts[1])

    K = []
    S = []
    T = []

    t = 0

    for i in range(N):
        parts = get_line().split()
        k = int(parts[0])
        s = int(parts[1])
        t1 = (D - k) * 1.0 / s
        T.append(t1)
        if t1 > t:
            t = t1
        K.append(k)
        S.append(s)

    l = 0.0
    h = D / t

    for i in range(100):
        m = (l + h) / 2.0
        if (ok(m, D, N, T)):
            l = m
        else:
            h = m
    return (l + h) / 2.0


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
