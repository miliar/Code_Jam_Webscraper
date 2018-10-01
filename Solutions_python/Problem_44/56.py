import sys
import math
import re
import os
import time
from itertools import *
from pprint import pprint
# headers based on a previous solution of round1B of vlad

if len(sys.argv) != 2:
    print 'specify input file'
    exit()

startTime = time.clock()

fin = open(sys.argv[1])
fout = open(os.path.splitext(sys.argv[1])[0]+'.out','w')
def cm(flies,t):
    n=0
    sx,sy,sz=0,0,0
    for firefly in flies:
        x,y,z,vx,vy,vz = firefly
        sx+=x+vx*t
        sy+=y+vy*t
        sz+=z+vz*t
        n = n+1
    sx=sx/n
    sy=sy/n
    sz=sz/n
    return math.sqrt(sx*sx+sy*sy+sz*sz)
    
def solve():
    N = int(fin.readline())
    sx,sy,sz,svx,svy,svz=0,0,0,0,0,0
    flies = []
    for i in range(N):
        firefly=fin.readline().strip().split()
        x = float(firefly[0])
        y = float(firefly[1])
        z = float(firefly[2])
        vx = float(firefly[3])
        vy = float(firefly[4])
        vz = float(firefly[5])
        flies.append([x,y,z,vx,vy,vz])
        sx += x
        sy += y
        sz += z
        svx += vx
        svy += vy
        svz += vz
    n = svx*sx+svy*sy+svz*sz
    d = svx*svx+svy*svy+svz*svz
    if d==0:
       t = 0
    elif n > 0:
       t = 0
    else:
       t = -n/d
    dmin = cm(flies,t)
    print>>fout,dmin,t

numCases = int(fin.readline())
for caseNo in range(numCases):
    print '\b'*10,100*caseNo/numCases,'%',
    print>>fout, 'Case #%s:'%(caseNo+1),
    solve()

fin.close()
fout.close()

print '\b'*10+'it took %.1fs'%(time.clock()-startTime)

