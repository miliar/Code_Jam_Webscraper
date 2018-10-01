# -* coding:utf-8 -*-
#! /usr/bin/python

import sys
import math


input=sys.stdin.read()
inList=input.split('\n')
N=int(inList.pop(0))

def f(ts,n):
    res = 0
    flg = [0]*len(ts)
    # print ts
    for i in range(len(ts)):
        for j in range(i+1,len(ts)):
            for k in range(j+1,len(ts)):
                if i == j or j ==k or k == i: continue
                if flg[i] == 1 or flg[j] == 1 or flg[k] == 1: continue
                if ( ts[i][0] + ts[j][0] + ts[k][0] )%3 == 0 and (ts[i][1] + ts[j][1] + ts[k][1]) % 3 == 0:
                    tmp = [(ts[i][0] + ts[j][0] + ts[k][0])/3, (ts[i][1] + ts[j][1] + ts[k][1])/3 ]
                    if tmp in ts:
                        if flg[ ts.index(tmp) ] == 1:
                            continue
                    res+=1
                    #flg[i] = 1
                    #flg[j] = 1
                    #flg[k] = 1
                    


    return res

for i in range(N):

    n, A, B, C, D, x0, y0, M = [ int(j) for j in  inList.pop(0).split()]

    X = x0
    Y = y0
    ts = [[X,Y]]
    for j in range(n-1):
        X = (A*X+B)%M
        Y = (C*Y+D)%M
        ts.append([X,Y])

    res = f(ts,n)
    print "Case #%d: %d"%(i+1, res)


    
