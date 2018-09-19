'''
Created on Sep 3, 2009

@author: Robin
'''
import string,sys

f=open('b.in', 'r')
mapCount = int(f.readline())

for i in range(mapCount):
    line = string.split(f.readline())
    converts = int(line[0])
    ind = 1
    convmap = {}
    opmap = {}
    for c in range(converts):
        s = line[ind]
        ind+=1
        convmap[s[:-1]] = s[2]
        convmap[s[1]+s[0]] = s[2]
    ops = int(line[ind])
    ind+=1
    for c in range(ops):
        s = line[ind]
        ind+=1
        opmap[s[0]] = s[1]
        opmap[s[1]] = s[0]
    
    spell = line[ind+1]    
    tray = []
    for s in spell:
        tray += s
        b = False
        if len(tray) > 1:
            l2 = tray[-2]+tray[-1]
            if str(l2) in convmap:
                tray = tray[:-2]+[convmap[l2]]
                b = True
        if not b:
            for other in tray:
                if other in opmap and opmap[other] == s:
                    tray = []
    
    
    
    sys.stdout.write("Case #"+str(i+1)+": [")
    for t in range(len(tray)):
        sys.stdout.write(tray[t])
        if t != len(tray)-1:
            sys.stdout.write(", ")
    print "]"
        
        
        