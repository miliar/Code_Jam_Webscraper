# -*- coding: utf-8 -*-
import sys
import math
from copy import deepcopy



def apc(lists, num, ip):
    ct = 0
    #if num==1000:
    #    for i in lists:
    #        if i[0]%3!=0:
    #            ct += 1
    #else:
    cop = deepcopy(lists)
    tmp = 0
    for idx, val in enumerate(cop):
        if tmp != num:
            nok = val[0] % 3
            if nok==0:
                cop[idx][3] += 1
                cop[idx][1] -= 1
                tmp += 1
            elif nok==1:
                pass
            else:
                cop[idx][3] += 1
                cop[idx][2] -= 1
                tmp += 1
            
    #print cop
    for i in cop:
        if i[3] >= ip:
            ct += 1 
    return ct

f = open(sys.argv[1], 'r')
line = f.readline().strip()

f2 = open('out2.txt', 'w+')

for i in range( int(line) ):
    li = f.readline().strip().split(' ')
    n = li[0]
    s = li[1]
    p = li[2]
    ip = int(p)
    li = li[3:]

    if ip == 1:
        min = 1
    elif ip == 0:
        min = 0
    else:
        min = (ip-2)*3 + 2
    
    res = []
    count = 0
    for j in li:
        if int(j) >= min:
            #print j, min
            nok = int(j) % 3
            avg = int(j) / 3
            if nok == 0:
                res.append( [int(j),avg,avg,avg] )
            elif nok == 1:
                res.append( [int(j),avg,avg,avg+1] )
            else:
                res.append( [int(j),avg,avg+1,avg+1] )
            count += 1
        
    
    res = sorted(res)
    #print res
    ss = "Case #%d: %d" % ( int(i)+1, apc(res, int(s), ip) )
    print ss
    f2.write(ss+"\r\n")
