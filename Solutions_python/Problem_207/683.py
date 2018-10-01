#!/usr/bin/env python
import numpy as np


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
t = int(inFile.readline())
for test in range(1, t+1):
    N, R, O, Y, G, B, V = map(int, inFile.readline().split(' '))
    ans = ['']*N
    available = {'R': R,
                 'Y': Y,
                 'B': B,
                 'G': G,
                 'O': O,
                 'V': V}
    keys = dict((v, k) for k, v in available.iteritems())
    fill = max(available.values())
    toUse = keys[fill]
    # possible = True
    remaining = ['R', 'Y', 'B']
    if(fill > N/2):
        outFile.write("Case #{}: IMPOSSIBLE\n".format(test))
        # print 'IMPOSSIBLE'
        continue
    positions = [2*x for x in range(fill)]
    last = positions[-1] + 2
    # print toUse
    # print positions
    for x in positions:
        ans[x] = toUse
    # print ans
    remaining.remove(toUse)
    toUse = remaining[0]
    fill = available[toUse]
    nextPos = last
    positions = []
    for i in range(fill):
        if(nextPos > N-1):
            nextPos = 1
        positions.append(nextPos)
        nextPos += 2
    # print toUse
    # print positions
    for x in positions:
        ans[x] = toUse
    # print ans
    toUse = remaining[-1]
    # prev = -5
    for i in range(len(ans)):
        # cur = 0
        if(not ans[i]):
            # cur = i
            ans[i] = toUse
    outFile.write("Case #{}: {}\n".format(test, ''.join(ans)))
