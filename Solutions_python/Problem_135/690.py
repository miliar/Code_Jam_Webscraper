# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring


        
ex = """3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
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
board = []
for i in range(T):
    r0 = int(lines[cursor])-1
    a00 = [int(l) for l in lines[cursor+1].split()]
    a01 = [int(l) for l in lines[cursor+2].split()]
    a02 = [int(l) for l in lines[cursor+3].split()]
    a03 = [int(l) for l in lines[cursor+4].split()]
    cursor += 5
    a0 = [a00,a01,a02,a03]
    r1 = int(lines[cursor])-1
    a10 = [int(l) for l in lines[cursor+1].split()]
    a11 = [int(l) for l in lines[cursor+2].split()]
    a12 = [int(l) for l in lines[cursor+3].split()]
    a13 = [int(l) for l in lines[cursor+4].split()]
    cursor += 5
    a1 = [a10,a11,a12,a13]
    
    result = ''
    first   = a0[r0]
    second  = a1[r1]
    
    cnt=0
    for f in first:
        if f in second:
            cnt+=1
            result = str(f)
    if cnt==0:
        result='Volunteer cheated!'
    elif cnt>1:
        result='Bad magician!'
    
#    cnt=0
#    for f in first:
#        if f in second:
#            cnt+=1
#    if cnt==0:
#        result = "Volunteer cheated!"
#    
#    if result=='':
#        for r in a1:
#            cnt=0
#            for f in first:
#                if f in r:
#                    cnt+=1
#            if cnt!=1:
#                result = "Bad magician!" 
#        
#        if result=='':
#            for f in first:
#                if f in second:
#                    result = str(f)
    
    jamout("Case #%d: %s" % (i+1, result))

if istest==False:
    fo.close()