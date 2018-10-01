#!/usr/bin/python

# My first idea: if everything has a row/col in which nothing is higher than it,
# than the lawn is possible.

#input: a file with input specs...
import sys


# This will take n^3 time.
def eval(lawnArr, nr, nc, caseNum):
    outStr = 'Case #{}: '.format(caseNum)
    #print outStr
    #print lawnArr
    for row in range(nr):
        for col in range(nc):
            passed = False
            curVal = lawnArr[row][col]
            # Looks through the col.
            cblockerExists = False
            for tmpRow in range(nr):
                if lawnArr[tmpRow][col] > curVal:
                    cblockerExists = True
            
            rblockerExists = False
            for tmpCol in range(nc):
                if lawnArr[row][tmpCol] > curVal:
                    rblockerExists = True
            
            if cblockerExists and rblockerExists:
                # both sides blocked, we're bad!
                print outStr + 'NO'
                return
    print outStr + 'YES'

# Read in the file, take care of formatting...
fName = sys.argv[1]
ff = open(fName)
allLines = ff.readlines()
numCases = int(allLines[0])

lastEndLine = 0
for case in range(numCases):
    caseDims = allLines[lastEndLine + 1].split()
    numRows = int(caseDims[0])
    numCols = int(caseDims[1])
    
    lawnArr = list()
    for row in range(numRows):
        lawnArr.append(map(int, allLines[lastEndLine + row + 2].split()))
    eval(lawnArr, numRows, numCols, case + 1)

    lastEndLine = lastEndLine + numRows + 1
        
        
