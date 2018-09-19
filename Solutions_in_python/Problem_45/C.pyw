
# -*- coding: cp949 -*-

import sys, copy

global g_cache, minv
def get_min(cells, tbr, v):
    global minv
    if(len(tbr) == 0):
##        cur = tbr[0]
##        v = v + cells[cur+1:].count(1)+cells[:cur].count(1)
        if(minv == -1 or v < minv):
            minv = v
    else:
        for i in range(len(tbr)):
            cur = tbr.pop(i)
            cells[cur] = 0
            tv = 0
            for c in cells[cur+1:]:
                if(c == 1):tv = tv+1
                else: break
            for j in range(cur-1, -1, -1):
                if(cells[j] == 1): tv = tv+1
                else: break
            get_min(cells, tbr, v+tv)
            cells[cur] = 1
            tbr.insert(i, cur)
    
if(len(sys.argv) == 1):
    fin = open("ex3.in", 'r')
    fout = open("ex3.out", 'w')
else:
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[2], 'w')

N = fin.readline().rstrip('\r\n')
N = int(N)

for i in range(N):
    P,Q = fin.readline().rstrip('\r\n').split()
    P,Q = int(P),int(Q)
    tbr = fin.readline().rstrip('\r\n').split()
    for j in range(len(tbr)):
        tbr[j] = int(tbr[j])-1
    cells = [1]*P
#    g_cache = [[-1]*len(l) for i in range(len("welcome to code jam"))]
    minv = -1
    get_min(cells, tbr, 0)
    fout.write("Case #%d: %d\n" % (i+1, minv))
    print(i)

fin.close()
fout.close()
