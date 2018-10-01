#!/usr/bin/env python

t = int(raw_input())

for i in range(t):
    parts = map(int,raw_input().split(' '))
    n = parts[0]
    s = parts[1]
    p = parts[2]
    tis = parts[3:]
    nupgradeable = 0
    ngreater = 0
    for ti in tis:
        mod = ti % 3
        maxscore = int(ti/3. - 0.1) + 1
        if ti == 0: 
            maxscore = 0
        if mod == 0 and maxscore == p-1 and maxscore > 0:
            nupgradeable += 1
        elif mod == 2 and maxscore == p-1 and maxscore > 0:
            nupgradeable += 1
        elif maxscore >= p:
            ngreater += 1
    ans = min(s, nupgradeable) + ngreater
    print "Case #%d: %d" %(i+1,ans)

