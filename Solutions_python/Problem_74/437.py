#!/usr/bin/python
# -*- coding: utf-8 -*-

import re,sys



if len(sys.argv) !=2:
    sys.exit()

f = open(sys.argv[1],"r")
i = 0
T = 0
for line in f:
    i = i + 1
    if i == 1:
        T = line
    else:
        case = line.strip().split(" ")
        num = int(case[0])
        actions = []
        for j in range(1,num+1):
            res = []
            res= [case[2 * j - 1], int(case[2 * j])]
            actions += [res,]
        #print actions

        lastpos = {'O' : 1, 'B' : 1}
        lasttime = {'O' : 0, 'B' : 0}
        curtime = 0
        
        for a in actions:
            #print a
            deltapos = abs(a[1] - lastpos[a[0]])
            if curtime > deltapos + lasttime[a[0]]:
                curtime = curtime + 1
            else:
                curtime = deltapos + lasttime[a[0]] + 1
            lastpos[a[0]] = a[1]
            lasttime[a[0]] = curtime
            #print lastpos,lasttime,curtime
        print "Case #%d:" % (i-1), curtime

f.close()




