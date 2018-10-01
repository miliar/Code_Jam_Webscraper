#!/usr/bin/env python

import os, sys


def solve (line):
    n = line[0]
    s = line[1]
    p = line[2]
    tp = line[3:]
    tp.sort()
    tp.reverse()

    pmax = 0
    resttp = []
    for t in tp:
        r = t%3
        d = t/3
        if p == 0:
            pmax += 1
        elif t == 0:
            continue
        elif r == 1 or r == 2:
            if d+1 >= p:
                pmax += 1
            else:
                resttp.append(t)
        elif  r == 0:
            if d >= p:
                pmax += 1
            else:
                resttp.append(t)

    for t in resttp:
        if not s:
            break
        r = t%3
        d = t/3
        if r == 2:
            if d+2 >= p:
                pmax += 1
                s -= 1
        elif r == 0:
            if d+1 >= p:
                pmax += 1
                s -= 1
        

    return str(pmax)


fd = sys.stdin

line = fd.readline()
sets = int(line)+1

for case in range(1, sets):
    line = [int(x) for x in fd.readline().strip().split()]
    nline = solve(line)
    print "Case #%s: %s" % (case, nline)

fd.close()
