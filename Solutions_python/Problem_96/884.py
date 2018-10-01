#!/usr/bin/env python
import math

N = int(raw_input())
for t in range(1,N+1):
    test = raw_input().split()
    n = int(test[0])
    s = int(test[1])
    p = int(test[2])

    point = [int(test[k]) for k in range(3,len(test))]
    point.sort()
    point.reverse()

    board = {}
    for x in range(n):
        v = point[x]
        a = v/3
        b = (v-a)/2
        c = v-a-b
        vv = [a,b,c]
        vv.sort()
        vv.reverse()
        if s>0:
            if vv[0]!=0 and vv[0] < p and vv[0]==vv[1]:
                vv[0]=vv[0]-1
                vv[1]=vv[1]+1
                s-=1
            elif vv[1]!=0 and vv[0] < p and vv[1]==vv[2]:
                vv[1]=vv[1]-1
                vv[2]=vv[2]+1
                s-=1
        
        board[x] = vv
    r = 0
    for xx in board.keys():
        if max(board[xx],key=int)>=p:
            r+=1

    print 'Case #'+str(t)+':',r 

