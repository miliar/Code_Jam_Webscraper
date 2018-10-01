#!/usr/bin/python

import sys


def isRecycled(a, b):
    aStr = str(a)
    bStr = str(b)
    if (len(aStr) == len(bStr)
        & len(aStr) > 1):
        for i in range(len(aStr)):
            if (aStr == bStr):
                return True
            else:
                aStr = aStr[1:] + aStr[0]
    ##else is not recycled
    return False


numberOfLines = int(sys.stdin.readline())

for i in range(numberOfLines):
    inputLine = sys.stdin.readline().strip()
    
    words = inputLine.split()
    lower = int(words[0])
    upper = int(words[1])
    
    
    pairs = 0
    searchUpper = upper
    while searchUpper >= lower:
        searchLower = lower
        while searchLower < searchUpper:
            if isRecycled(searchLower,searchUpper):
                pairs +=1
            searchLower+=1
        searchUpper-=1
        
    
#    print str(words)
#    print str(isRecycled(3, 4))
#    print str(isRecycled(30, 4))
#    print str(isRecycled(30, 30))
#    print str(isRecycled(12345, 34512))
    print "Case #%s: %s" % (i+1, str(pairs))

