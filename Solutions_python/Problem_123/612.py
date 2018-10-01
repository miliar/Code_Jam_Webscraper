# Python version 2.7
import sys

def stopIndex(a,ms):
    x = a
    for i,m in enumerate(ms):
        if m < x: x+= m
        else: return i
    return None

def addNumbers(a,ms,i):
    s = sum(ms[0:i])
    x = a+s
    if x<=1: return None
    r = []
    while x <= ms[i]:
        r.append(x-1)
        x += x-1
    return r

def oneCase():
    [a,n] = map(int, sys.stdin.readline().split(' '))
    ms = map(int, sys.stdin.readline().split(' '))
    ms.sort()
    x = 0
    i = 0
    while stopIndex(a,ms) != None:
        #print a,ms
        i = stopIndex(a,ms)
        #print i
        r = addNumbers(a,ms,i)
        if r==None: return str(x+(n-i))
        if len(r) < n-i:
            x += len(r)
            ms_ = ms[0:i]+r+ms[i:len(ms)]
            ms = ms_
            n = len(ms)
        else: return str(x+(n-i))
    #print ms
    return str(x)
    

cases = int(sys.stdin.readline())
for i in range(cases):
    print "Case #" + str(i+1) + ": " + oneCase() 