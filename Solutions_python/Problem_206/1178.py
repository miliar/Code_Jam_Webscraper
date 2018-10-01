#!/bin/python

def findMaxCruiseCtrlSpeed(dist, posns, speeds):
    n = len(posns)
    arrTimes = map(lambda p, s: (dist - p)/float(s), posns, speeds)
    latestTime = 0
    bottleneck = -1
    for i in xrange(n-1, -1, -1):
        if arrTimes[i] > latestTime:
            latestTime = arrTimes[i]
            bottleneck = i
    return dist/latestTime

t = int(raw_input().strip())
for test in xrange(1, t+1):
    d, n = map(int, raw_input().strip().split(' '))
    posns = [0] * n
    speeds = [0] * n
    for i in xrange(n):
        k, s = map(int, raw_input().strip().split(' '))
        posns[i] = k
        speeds[i] = s
    ccspd = findMaxCruiseCtrlSpeed(d, posns, speeds)
    print ("Case #%d: %f" % (test, ccspd)) 
