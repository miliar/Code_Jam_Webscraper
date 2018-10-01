#!/usr/bin/python

import sys,re


blank = re.compile("^\s+$")

fin = file(sys.argv[1])
linecount = int(fin.readline().strip())

f = open('output.txt', 'w')
for i in xrange(0,linecount):
    line = fin.readline().rstrip().split() 
    n = int(line[0])
    s = int(line[1])
    p = int(line[2])
    count = 0
    mini = 3*p-4;
    maxi = 3*p-2;
    if mini<0 :
        mini=0
    if maxi<0 :
        maxi=0
    for j in xrange(n):
        num = int(line[3+j])
        if num == 0:
            if p == 0:
                count +=1
            else:
                continue
        elif num >= maxi:
            count += 1
            continue
        elif num < mini: 
            continue;
        else:
            if s > 0:
                count += 1
                s -= 1
                continue
    print count

    if i+1 == linecount:
        f.write('Case #'+str(i+1)+': '+str(count))
    else :
        f.write('Case #'+str(i+1)+': '+str(count)+"\n")
f.close()
