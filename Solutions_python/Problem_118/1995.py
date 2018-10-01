from math import floor

def isSquare(n):
    s = n ** .5
    return s - floor(s) == 0

def isPalindrome(n):
    nStr = str(n)
    ln = len(nStr)
    isPal = True
    for c in xrange(0, ln / 2):
        if nStr[c] != nStr[ln - c - 1]:
            isPal = False
            break
    return isPal

def solve(cases, inFile, outputFile):
    for c in xrange(1, cases + 1):
        bounds = inFile.readline().split()
        print 'bounds:', bounds
        fairAndSquare = 0
        for checkNum in xrange(int(bounds[0]), int(bounds[1]) + 1):
            if isSquare(checkNum) and isPalindrome(checkNum):
                if isPalindrome(int(checkNum ** .5)):
                    fairAndSquare += 1
        outputFile.write("Case #" + str(c) + ": " + str(fairAndSquare))
        outputFile.write('\n')

inFile = open('C-small-attempt0.in')
outputFile = open('output.txt', 'w')

cases = int(inFile.readline())
print cases, 'cases read'

solve(cases, inFile, outputFile)
print 'done'

inFile.close()
outputFile.close()