#!/usr/bin/python

import sys

cases = int(sys.stdin.readline())
for case in range(1,cases+1):
    v = map(int, sys.stdin.readline().rstrip().split(' '))
    N = v[0]
    M = v[1]
    lawn = []
    cuts = []
    W = "YES"
    for i in range(0,N):
        line = sys.stdin.readline().rstrip().split(' ')
        Max = max(line)
        if Max != line[0]:
            cuts.append(Max)
        else:
            cuts.append(line[0])
        lawn.append(line)
    i = 0
    while i < M and W == "YES":
        col = [line[i] for line in lawn]
        Max = max(col)
        cut = line[0]
        if Max != cut:
            cut = Max
        j = 0
        while j < N and W == "YES":
            if col[j] != cut and cuts[j] != col[j]:
                W = "NO"
            j = j + 1
        i = i + 1
    print "Case #"+str(case)+": "+str(W)
