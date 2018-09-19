#!/usr/bin/python

from math import sqrt

tasknum=int(raw_input())

def isitpalindrome(num):
    numstr=str(num)
    for i in range(len(numstr)/2):
        if(numstr[i]!=numstr[len(numstr)-i-1]):
            return False
    return True

for taski in range(tasknum):
    start,end=[int(x) for x in raw_input().split(" ")]
    
    count=0

    startsqrt=sqrt(start)
    if(startsqrt>int(startsqrt)):
        startsqrt=int(startsqrt+1)
    else:
        startsqrt=int(startsqrt)

    endsqrt=int(sqrt(end))

    for cur in range(startsqrt,endsqrt+1):
        if(not isitpalindrome(cur)):
            continue
        cursquared=cur**2
        if(not isitpalindrome(cursquared)):
            continue
        count+=1

    print("Case #%s: %s"%(taski+1,count))
