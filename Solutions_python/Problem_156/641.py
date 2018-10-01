__author__ = 'knusper'
import math
import sys

def readint(ip):
    return int(ip.readline())
def readintlist(ip):
    return list(map(int,ip.readline().split()))
def readintset(ip):
    return set(map(int,ip.readline().split()))
def readfloat(ip):
    return float(ip.readline())
def readfloatlist(input):
    return list(map(float,ip.readline().split()))
def readstring(ip):
    return ip.readline().strip()
def writeanswer(op,t,sol):
    op.write("Case #"+str(t)+": "+str(sol)+"\n")

fn="B-large"

ip = open(fn+".in", 'r')
op = open(fn+".out", "w")

for t in range(1,readint(ip)+1):
    D=readint(ip)
    P=readintlist(ip)
    #P.sort()
    #average=sum(P)/D
    minimum=1001
    for x in range(1,max(P)+1):
        moves=[math.ceil(P[i]/x) for i in range(len(P))]
        for i in range(len(moves)):
            moves[i]=moves[i]-1
        total=sum(moves)+x
        if total<minimum:
            minimum=total
    writeanswer(op,t,minimum)
op.close()