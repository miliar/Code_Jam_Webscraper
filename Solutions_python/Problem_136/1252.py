#!/usr/bin/python
import sys
fin = open("B-large.in", "r")
line = fin.readline()
testcase = int(line)
ans=0.0
for i in range(testcase): #i is testcase
    r = 2.0
    t = 0.0
    b = 0
    splitline = fin.readline().split(' ')
    splitline[2] = splitline[2].rstrip('\n')
    #print(splitline)
    c = float(splitline[0])
    f = float(splitline[1])
    x = float(splitline[2])
    while (t+x/r)>(t+(c/r)+x/(r+f)):
        t+=c/r #build a factory
        r+=f
        b+=1
    t+=x/r
    ans=round(t,7)
    print('Case #'+str(i+1)+': '+str(ans))
