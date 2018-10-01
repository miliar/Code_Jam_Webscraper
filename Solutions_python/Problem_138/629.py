# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring


        
ex = """4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
"""

if len(sys.argv)==3:
    infile  = sys.argv[1]
    outfile = sys.argv[2]
    fo = open(outfile,'w')
    s = open(infile, 'r').read()
    lines = s.split('\n')
    istest = False
else:
    lines = ex.split('\n')
    istest = True

T = int(lines[0])
cursor = 1
for i in range(T):
    N = int(lines[cursor])
    nao = [float(l) for l in lines[cursor+1].split( )]
    ken = [float(l) for l in lines[cursor+2].split( )]
    cursor += 3
    
    nao.sort()
    ken.sort()
    tmp_nao = nao[:]
    tmp_ken = ken[:]
    
    cnt_w = N
    for n in range(N):
        ischosen = False
        for t in tmp_ken:
            if t>nao[n]:
                ischosen=True
                cnt_w-=1
                tmp_ken.remove(t)
                break
        if not ischosen:
            tmp_ken.pop(0)
    
    tmp_nao = nao[:]
    tmp_ken = ken[:] 
    cnt_d=0
    for n in range(N):
        if tmp_nao[-1]>tmp_ken[-1]:
            cnt_d+=1
            tmp_nao.pop()
            tmp_ken.pop()
        else:
            tmp_nao.pop(0)
            tmp_ken.pop()
    

    jamout("Case #%d: %d %d" % (i+1, cnt_d, cnt_w))

if istest==False:
    fo.close()