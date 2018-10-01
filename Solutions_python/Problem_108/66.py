#!/usr/bin/python3

from sys import argv

infile = open(argv[1])
cases = int(infile.readline())
for i in range(cases):
    n = int(infile.readline())
    vine = []
    for j in range(n):
        vine.append(list(map(int, infile.readline().split())))
    d = int(infile.readline())
    f = []
    if vine[0][0] > vine[0][1]:
        f.append(0)
    else:
        f.append(2 * vine[0][0])
    for j in range(1, n):
        for k in range(0, j):
            f.append(0)
            # f[k] is the farthest you can reach having taken rope k last
            # compute how far you could get with taking rope j
            if vine[j][0] <= f[k]:
                dist = vine[j][0] + min(vine[j][0] - vine[k][0],
                                        vine[j][1])
                if dist > f[j]: f[j] = dist
    possible = False
    for j in range(0, n):
        if f[j] >= d:
            possible = True
    print('Case #{}: {}'.format(i+1, "YES" if possible else "NO"))
