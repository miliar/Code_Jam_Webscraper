#!/usr/bin/env python
import sys

f=open('A-small-attempt0.in')
fo=open('A-small.out','w')
cases = f.readline().rstrip()
for a in range(1,int(cases)+1):
    frow=()
    srow=()
    fo.write("Case #%d: " % a)
    firstchoice = int(f.readline().rstrip())
    for b in range(4):
        row = f.readline().rstrip()
        if (b == firstchoice-1):
            frow=row.split()
    secondchoice = int(f.readline().rstrip())
    for b in range(4):
        row = f.readline().rstrip()
        if (b == secondchoice-1):
            srow=row.split()
    found = 0
    single = True
    for c in range(1,17):
        if(str(c) in frow and str(c) in srow):
            if(found > 0):
                single = False
            found = c
    if(found > 0 and single):
        fo.write(str(found)+'\n')
        next
    if(not single):
        fo.write("Bad magician!\n")
        next
    if(found == 0):
        fo.write("Volunteer cheated!\n")
fo.close()
f.close()
            
            
        
