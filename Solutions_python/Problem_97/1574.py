# cRecycledNumbersHelper.py
# https://code.google.com/codejam/contest/1460488/dashboard#s=p2
# by John Shaffstall aka double051

import shlex
import os

class memoize:
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]

@memoize
def getCharSet(aString):
    return set(aString[:])

@memoize
def recycledStrings(strings):
    aStr = strings[0]
    bStr = strings[1]
    aSet = getCharSet(aStr)
    bSet = getCharSet(bStr)
    aLen = len(aStr)
    # print aStr, aSet, bStr, bSet
    if aLen == len(bStr) and aSet == bSet:
        for i in xrange(0, aLen):
            cStr = '%s%s'%(''.join(aStr[i:aLen]), ''.join(aStr[0:i]))
            # print cStr, bStr
            cInt = int(cStr)
            bInt = int(bStr)
            aInt = int(aStr)
            if cInt == bInt and cInt >= aInt:
                # print cInt, bInt, aInt
                return 1
    return 0

@memoize
def recycledNumbers(numbers):
    a = numbers[0]
    b = numbers[1]
    print a, b
    count = 0
    for i in xrange(a, b):
        a = i
        while a < b:
            count = count + recycledStrings((str(a),str(b)))
            b = b - 1
        b = numbers[1]
    print 'count = ', count
    return count

outputFile = open('cTestSampleOutput.txt', 'w+')

inputs = []
with open('C-small-attempt0.in') as inputFile:
    inputCount = int(inputFile.readline().rstrip())
    for i in xrange(0, inputCount):
        inputLine = inputFile.readline().rstrip()
        print inputLine
        lineStrings = shlex.split(inputLine)
        print lineStrings
        lineInts = tuple(int(a) for a in lineStrings if a.isdigit())
        inputs.append(lineInts)
print inputs

# max of 50 inputs
# input[0] and input[1] have the same number of inputs
outputs = map(recycledNumbers, inputs);

with open('C-small-attempt0.out', 'w+') as outputFile:
    for i in xrange(0, len(outputs)):
        outputFile.write('Case #%d: %d\n'%(i+1, outputs[i]))