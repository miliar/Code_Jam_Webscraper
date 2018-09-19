import sys
import psyco
import re
psyco.full()

l,d,n=map(int,sys.stdin.readline().split(' '))

wordlist=[]
for i in range(d):
    wordlist.append(sys.stdin.readline()[:-1])

for i in range(n):
    pattern=sys.stdin.readline()[:-1].replace('(','[').replace(')',']')
    pobj=re.compile(pattern)
    count=0
    for j in wordlist:
        if pobj.match(j):
            count+=1
    print "Case #%s: %s"%(i+1,count)
