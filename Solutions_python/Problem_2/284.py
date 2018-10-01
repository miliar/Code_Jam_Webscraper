#!/usr/bin/python
#
# Google Code Jam 2008
# Submission: nicholas.cw.ng@gmail.com

from datetime import time
import sys
n = int(sys.stdin.readline()) # number of cases

for case in range(0, n): # cases
    t = int(sys.stdin.readline()) # turnaround time
    na, nb = map(int, sys.stdin.readline().split())

    stna = {}
    stnb = {}
    for triptime in range(0, na+nb): # trips
        depart, arrive = map(lambda str: map(int,str.split(':')),sys.stdin.readline().split())
        arrive[1] += t # plus turnaround time
        if arrive[1] >=60:
            arrive[1]-=60
            arrive[0]+=1
        if arrive[0] >=24:
            arrive[0]=23
            arrive[1]=59

        if depart[1] >=60:
            depart[1]-=60
            depart[0]+=1
        if depart[0] >=24:
            depart[0]=23
            depart[1]=59


        at = time(arrive[0], arrive[1])
        dt = time(depart[0], depart[1])
       

        if triptime>=na:
            if not stna.has_key(at.strftime("%H%M")):
                stna[at.strftime("%H%M")] = 0
            if not stnb.has_key(dt.strftime("%H%M")):
                stnb[dt.strftime("%H%M")] = 0
            stna[at.strftime("%H%M")] -= 1 
            stnb[dt.strftime("%H%M")] += 1
        else:
            if not stna.has_key(dt.strftime("%H%M")):
                stna[dt.strftime("%H%M")] = 0
            if not stnb.has_key(at.strftime("%H%M")):
                stnb[at.strftime("%H%M")] = 0
            stna[dt.strftime("%H%M")] += 1
            stnb[at.strftime("%H%M")] -= 1

    # get events in time sequence
    keysa = stna.keys()
    keysa.sort()
    keysb = stnb.keys()
    keysb.sort()

    # events in Station A
    a_max = 0
    curr = 0
    for event in [stna[k] for k in keysa]:
        curr += event
        if curr >= a_max:
            a_max = curr

    # events in Station B
    b_max = 0
    curr = 0
    for event in [stnb[k] for k in keysb]:
        curr += event
        if curr >= b_max:
            b_max = curr

    print "Case #"+str(case+1)+":",a_max,b_max
