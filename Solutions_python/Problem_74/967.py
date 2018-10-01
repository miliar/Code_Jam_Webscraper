# -*- coding: utf-8 -*-

import sys
import re

def timeit(case):
    moves=re.findall('[OB]\s[\d]+',case)
    t=0
    orange=1
    blue=1
    otime=0
    btime=0
    for move in range(int(case[:case.find(' ')])):
        robot=moves[move][:1]
        button=int(moves[move][2:])
        
        if robot is 'O':
            move_time=abs(orange-button)
            move_time-=btime
            btime=0
            if move_time<0:
                move_time=0
            orange=button
            otime+=move_time+1
        elif robot is 'B':
            move_time=abs(blue-button)
            move_time-=otime
            otime=0
            if move_time<0:
                move_time=0
            blue=button
            btime+=move_time+1
        t+=move_time+1
            
        
    return t

fin = sys.stdin
#fin=open('local.txt')
for case in range(int(fin.readline())):
    tc=fin.readline()
    print 'Case #%d: %d' % (case+1, timeit(tc))
