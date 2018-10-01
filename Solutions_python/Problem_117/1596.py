#!/usr/bin/env python
import sys


def badRow(r):
    count = 0
    for i in r:
        if i == 1:
            count = count + 1
    if len(r) != count and count > 0:
        return True
    return False


def badCol(grass, c):
    col = [i[c] for i in grass]
    return badRow(col)

if len(sys.argv) == 1:
    f = sys.argv[0][:-2] + 'in'
if len(sys.argv) == 2:
    f = sys.argv[1]


lines = open(f, "r").readlines()
lines = list(map(lambda x: x.strip(), lines))
caseN = int(lines[0])


case = 0
i = 1
"""Starts from second line !!!"""
while case < caseN:
    ans = "YES"
    N = int(lines[i].split()[0])  # rows
    M = int(lines[i].split()[1])  # collums
    grass = []
    for j in range(1, N + 1):
        grass.append([int(x) for x in lines[i + j].split()])
    #for g in grass:
        #print(g)

    for j in range(N):
        for k in range(M):
            if grass[j][k] == 1:
                if badRow(grass[j]) and badCol(grass, k):
                    ans = "NO"
                    break
        if ans == "NO":
            break
    

   # for j, k in zip(range(N), range(M)):
        #print("Row", j, ":", badRow(grass[j]))
        #print("Col", k, ":", badCol(grass, k))
        #if 1 in grass[j] and 1 in [z[k] for z in grass]:
            #if badRow(grass[j]) and badCol(grass, k):
                #ans = "NO"
                #break
    case = case + 1
    print("Case #" + str(case) + ": " + ans)
    i = i + N + 1
