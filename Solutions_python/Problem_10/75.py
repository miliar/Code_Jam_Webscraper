import sys
import string
import math

inputfile=open(r'.\input.in', 'r')
numofcases=string.atoi(inputfile.readline())
for i in range(numofcases):
    [p,k,l]=map(lambda x: string.atoi(x), inputfile.readline().split())
    flist=map(lambda x: string.atoi(x), inputfile.readline().split())
    fmap=[]
    for j in range(l):
        fmap.append([j,flist[j]])
    fmap.sort(lambda x,y: cmp(y[1],x[1]))
    keys=[[] for m in range(k)]
    count=0
    for el in fmap:
        keys.sort(lambda x,y:cmp(len(x),len(y)))
        for ek in keys:
            if len(ek)<p:
                ek.append(el[0])
                count+=el[1]*len(ek)
                break
    print 'Case #%d: %d' %(i+1, count)
