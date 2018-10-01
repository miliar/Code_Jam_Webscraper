#!/bin/env python

from __future__ import print_function



def writeCase(theFile, caseNumber, answer):
    if answer is not None:
        theFile.write("Case #%d:\n"%caseNumber)
        line1 = ' '.join([str(x) for x in answer[0]])
        line2 = ' '.join([str(x) for x in answer[1]])
        theFile.write(line1 + "\n")
        theFile.write(line2 + "\n")
    else:
        theFile.write("Case #%d: Impossible"%caseNumber)
    return

def solveCase(theFile): # Don't forget: readline includes the \n
    theLine = [int(x) for x in theFile.readline().strip().split()]
    total = theLine[0]
    nums = theLine[1:total+1]
    sums = []
    newSums = []
    for num in nums:
        for ind, aSum in enumerate(sums):
            if num == aSum:
                print(ind, num, "first print")
                return (getSet(ind+1, nums), [num])
        newSums = [num]
        for lastInd, lastNum in enumerate(sums):
            newSum = num + lastNum
            for ind, aSum in enumerate(sums):
                if newSum == aSum:
                    print(ind, newSum, "second print")
                    return (getSet(ind+1, nums), getSet(lastInd+1, nums)+[num])
            newSums += [newSum]
        sums += newSums
    return None


def getSet(indicator, nums):
    result = []
    ctr = 0
    while indicator > 0:
        if (indicator&1):
            result += [nums[ctr]]
        indicator >>= 1
        ctr += 1
    return result

        
                


def main(fileName):
    f = open(fileName, "U")
    g = open(fileName+".out", "w")
    cases = int(f.readline())
    for x in xrange(cases):
        writeCase(g, x+1, solveCase(f))
    f.close()
    g.close()
    return

if __name__ == "__main__":
    from sys import argv
    main(argv[1])
