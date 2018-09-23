import math
import numpy as np
#import datetime
#import time


#fout = open('C:\\Users\\Soheil\\Documents\\Visual Studio 2017\\Projects\\gc20171C-A\\gc20171C-A\\Aoutput-small.out', 'w')
fout = open('C:\\Users\\Soheil\\Documents\\Visual Studio 2017\\Projects\\gc20171C-A\\gc20171C-A\\Aoutput-large.out', 'w')

def Surface(r):
    s=r*r*math.pi
    return s

def Border(r,h):
    b=2*r*math.pi*h
    return b

T=int(input())
for t in range(1,T+1):
    #print(t)
    N,K=map(int, input().split())
    
    l=[]
    for i in range(0,N):
        l.append(list(map(int, input().split())))
    l.sort(reverse=True)
    borders=[]
    for i in range(0,N):
        borders.append([Surface(l[i][0]),Surface(l[i][0])+Border(l[i][0],l[i][1]),Border(l[i][0],l[i][1])])
    borders.sort(reverse=True)
    #print(borders)

    area=[]
    for i in range(0,N-K+1):
        tarea=borders[i][1] 
        blist=[]
        for j in range(i+1,N):
            blist.append(borders[j][2])
        blist.sort(reverse=True)
        for j in range(0,K-1):
            tarea=tarea+blist[j]
        area.append(tarea)
    maxarea=max(area)        

    #area=Surface(l[0][0])+Border(l[0][0],l[0][1])
    #area=borders[0][0]
    #for i in range(1,K):
    #    area=area+borders[i][1]
    #print(area)

    fout.write("Case #{}: {}\n".format(t,maxarea))
fout.close()