
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

    R = int(parts[1])
    O = int(parts[2])
    Y = int(parts[3])
    G = int(parts[4])
    B = int(parts[5])
    V = int(parts[6])

    # R, Y, B

    m = {'R': R, 'Y': Y, 'B': B}

    seq = ['R', 'Y', 'B']
    if m[seq[0]] < m[seq[1]]:
        seq[0], seq[1] = seq[1], seq[0]
    if m[seq[0]] < m[seq[2]]:
        seq[0], seq[2] = seq[2], seq[0]
    if m[seq[1]] < m[seq[2]]:
        seq[1], seq[2] = seq[2], seq[1]

    #if m[seq[0]] * 2 > N:
    #    return "IMPOSSIBLE"

    #print seq
    #print m


    res = []
    for i in range(m[seq[1]]):
        res.append(seq[0])
        res.append(seq[1])

    for i in range(m[seq[0]] - m[seq[1]]):
        res.append(seq[0])


    num2 = m[seq[2]]
    newres = [res[0]]
    for i in range(1, len(res)):
        if res[i] == res[i-1]:
            if num2 == 0:
                return "IMPOSSIBLE"
            num2 -= 1
            newres.append(seq[2])
        newres.append(res[i])

    if newres[0] == newres[-1]:
        if num2 == 0:
            return "IMPOSSIBLE"
        num2 -= 1
        newres.append(seq[2])


    res = list(newres)

    while num2 > 0:
        found = False
        for i in range(len(res)):
            if res[i] != seq[2] and res[(i-1-len(res))%len(res)] != seq[2]:
                res.insert(i, seq[2])
                found = True
                break
        if not found:
            return "IMPOSSIBLE"
        num2 -= 1
        #print num2, ''.join(res)

    return ''.join(res)


T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
