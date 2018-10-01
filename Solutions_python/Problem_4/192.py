#!/usr/bin/python
import sys
import re

sys.setrecursionlimit(1500)

def process(numsA, curNums):
    ans = 0
    i = 0
    while i < len(numsA):
        ans = ans + numsA[i] * curNums[i]
        i = i + 1
    return ans

def calc( idx, numsA, numsB, curNums, curIdx, best ):
    if( len(curNums) == len(numsA) ):
        ans = process(numsA, curNums)
        if (ans < best):
            return ans
        else:
            return best
    
    i = 0
    while i < len(numsA): 
        if i not in curIdx:
            curIdx.append(idx)
            curNums.append(numsB[i])
            best = calc( idx + 1, numsA, numsB, curNums, curIdx, best)
            curNums.pop()
            curIdx.pop()
        i = i + 1
    return best



 #p = re.compile('.*hello.*', re.IGNORECASE)
f = open(sys.argv[1], 'r')

testCases = int(f.readline())

i=0
if( testCases <= 0 ):
    print "Case #" + str(i+1) + ": " + 0
else:

    while i < testCases:
        n = int(f.readline())
        numsAStr = f.readline().split()
        numsBStr = f.readline().split()
        
        x = 0
        while x < len(numsAStr):
            numsAStr[x] = int(numsAStr[x])
            numsBStr[x] = int(numsBStr[x])
            x = x + 1

        numsAStr = sorted(numsAStr)
        numsBStr = sorted(numsBStr)
        numsAStr.reverse()
      #best = calc( 0, numsAStr, numsBStr, [], [], 100000)
        best = process( numsAStr, numsBStr)
        print "Case #" + str(i+1) + ": " + str(best)
        
        i = i + 1



    #print "Line: " + line
    #mtch = p.match(line)
    #if( mtch != None ):
    #    print mtch.group()



