import sys
import urllib2
import json
from time import sleep

fin = open( 'C-large.in', 'r')
fout = open( 'c.out', 'w')

cases = fin.readline()
nList = []

for i in range( 0, 2000001):
    #print i
    k = str(i)
    s = {}
    s[i] = 1
    for j in range( 0, len(str(i))-1):
        t = k[1:] + k[0]
        #print t
        s[int(t)] = 1
        k = t
    #print s.keys()
    nList.append( s)

print nList[1102].keys()
for i in range( int(cases)):
    line = fin.readline()
    A = line.split(' ')[0]
    B = line.split(' ')[1]
    ans = {}
    cnt = 0
    for j in range( int(A), int(B) + 1):
        g = nList[j].keys()
        for k in g:
            if k > j and k <= int(B):
                cnt = cnt + 1
    print "Case #" + str(i+1) + ": " + str(cnt)
    fout.write( "Case #" + str(i+1) + ": " + str(cnt) + '\n')
    
fout.close()
fin.close()

