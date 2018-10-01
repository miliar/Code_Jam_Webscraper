__author__ = 'krzsza'

import csv
import math


def parseInput(inputFile):
    # opens input file with names
    inputFile = open(inputFile, 'r')
    arrayIntervals = []

    # reading space delimiting file and appending contents to array
    readerCSV = csv.reader(inputFile, delimiter=' ', quotechar='"', skipinitialspace=True)
    for readLine in readerCSV:
        arrayIntervals.append(map(int, readLine))

    # closing file and returning array
    inputFile.close

    return (arrayIntervals)


def isWhole(x):
    if (x % 1 == 0):
        return True
    else:
        return False


def isPalindrome(x):
    string = str(x)
    if string == string[::-1]:
        return True
    else:
        return False


arrInput = parseInput('C-small-attempt0.in')
testCasesNo = arrInput[0][0]
arrTestResult = []

for i in range(1, testCasesNo + 1):
    fairSquareNo = 0
    for y in range(arrInput[i][0], arrInput[i][1] + 1):
        if isPalindrome(y) == True:
            if isWhole(math.sqrt(y)) == True:
                if isPalindrome(int(math.sqrt(y))) == True:
                    fairSquareNo += 1
    arrTestResult.append(fairSquareNo)

for i in range (0, len(arrTestResult)):
    print "Case #%d: %d " % (i + 1, arrTestResult[i])