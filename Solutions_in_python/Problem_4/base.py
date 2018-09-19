#!/usr/bin/python

import sys
from processing import Process, Queue, Manager

def extract_data(fd):
    line = fd.readline()[:-1]
    ####### Code here #######
   
    n = int(line)

    line = fd.readline()[:-1]
    V1 = map(int,line.split(" "))

    line = fd.readline()[:-1]
    V2 = map(int,line.split(" "))

    #num1 = int(line.split(" ")[1])
    
    return (V1,V2)
    #########################

def resolve(V1,V2):
    ####### Code here #######
    V1.sort()
    V2.sort()
    V2.reverse()
    c =0
    for I in xrange(V1.__len__()):
        c += V1[I]*V2[I]

    return c
    #########################

#############################################
#############################################
#############################################
#############################################

def codejam():
    sys.setrecursionlimit(2000)
    process_number=2
    fd = open(sys.argv[1])
    n = int(fd.readline())



    data = []
    for I in xrange(n):
        data.append(extract_data(fd))
    fd.close()

    out = []
    for I in xrange(n):
        out.append("Case #%d: %d"%(I+1,resolve(data[I][0],data[I][1])))


    fd = open(sys.argv[2],"w")
    r = "\n".join(out)
    fd.write(r)
    return r


print "\n%s"%(codejam())
