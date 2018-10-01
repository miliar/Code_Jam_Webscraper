
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


def calc():
    parts = get_line().split()
    N = int(parts[0])
    Q = int(parts[1])
    E = []
    S = []
    for i in range(N):
        parts = get_line().split()
        E.append(int(parts[0]))
        S.append(int(parts[1]))
    #print N, Q
    #print E, S

    D = []
    for i in range(N):
        D.append([int(x)  for x in get_line().split()])
    #print D

    for i in range(Q):
        parts = get_line().split()
        s = int(parts[0])
        e = int(parts[1])
    #print Q

    culd = [0]
    for i in range(N - 1):
        culd.append(culd[-1] + D[i][i+1])

    #print culd

    f = [-1] * N
    f[N - 1] = 0
    for i in range(N - 2, -1, -1):
        t = -1
        for j in range(i + 1, N):
            if E[i] >=  culd[j] - culd[i]:
                t1 = (culd[j] - culd[i]) * 1.0 / S[i]
                if f[j] != -1:
                    if t == -1 or f[j] + t1 < t:
                        t = f[j] + t1
            else:
                break
        f[i] = t
        #print i, f[i]
    return f[0]


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
