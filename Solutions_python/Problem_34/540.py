#!/usr/bin/python

import sys
        
lines = sys.stdin.readlines()
info = lines[0]

(L, D, N) = info.split(' ')
L = int(L)
D = int(D)
N = int(N)

dict = []
for l in lines[1:D+1]:
    dict.append(l[:-1])

allwds = []
case = 1
for wd in lines[D+1:]:

    wdchs = []
    curchs = []
    inclass = False
    idx = 0
    for ch in wd:
        if idx >= L: break
        if ch == '(':
            inclass = True
        elif ch == ')':
            wdchs.append(curchs)
            curchs = []
            idx += 1
            inclass = False
        else:
            curchs.append(ch)
            if not inclass:
                wdchs.append(curchs)
                curchs = []
                idx += 1 
                
    safe = dict
    index = 0

    for grp in wdchs:
        safe = [x for x in safe if x[index] in grp]
        index+= 1

    print "Case #" + str(case) + ': ' +  str(len(safe))
    case+= 1
    
    

