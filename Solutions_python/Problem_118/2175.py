__author__ = 'cmoravec'
import math
import multiprocessing
import sys


def isFair(inNumber):
    inString = str(inNumber)
    sLen = len(inString)
    if sLen == 1:
        return True
    if sLen % 2 == 0:
        #even number of characters
        sLenHalf = sLen / 2
        if inString[0:sLenHalf] == inString[sLenHalf:][::-1]:
            return True
        return False
    else:
        sLenHalf = (sLen - 1) / 2
        if inString[0:sLenHalf] == inString[sLen - sLenHalf:][::-1]:
            return True
        return False

def testRange(minNum, maxNum):
    fairAndSquareCount = 0
    fairAndSquareList = []
    #find the first fair number that has a fair root that is an integer
    testNum = None
    num = minNum
    #for num in range(minNum, maxNum + 1):
    while num <= maxNum:
        if isFair(num):
            #print "Fair: {}".format(num)
            testNum = math.sqrt(num)
            if testNum % 1 == 0:
                testNum = int(testNum)
                if isFair(testNum):
                    fairAndSquareCount += 1
                    fairAndSquareList.append(num)
                    break
        num += 1

    if testNum is None:
        return 0
    #print "Found first number: {}".format(fairAndSquareList[0])
    #starting at testNum (the root of the first fair and square, add 1
    #until you find the next Fair number, and then square it and see if it is fair also
    testNum += 1
    while (testNum * testNum) <= maxNum:
        if isFair(testNum):
            testSquare = testNum * testNum
            if isFair(testSquare):
                if testSquare not in fairAndSquareList:
                    fairAndSquareList.append(testSquare)
                    fairAndSquareCount += 1
        testNum += 1

    return fairAndSquareCount

def testRangeWrapper(data):
    return testRange(data[0], data[1])

def testRangeTreading(minNum, maxNum):
    if maxNum - minNum <= 100000:
        return testRange(minNum, maxNum)
    threads = 4
    section = int(round((maxNum - minNum) / threads))
    groups = list()
    groups.append([minNum, minNum + section])
    groups.append([minNum + section + 1, minNum +(section * 2)])
    groups.append([minNum + (section * 2) + 1, minNum + (section * 3)])
    groups.append([minNum + (section * 3) + 1, maxNum])
    print groups
    p = multiprocessing.Pool(processes=threads)
    result = p.map(testRangeWrapper, groups)
    p.close()
    p.join()
    print result.get()



def readFile(pathToFile, writeFile):
    calcList = []
    with open(pathToFile) as f:
        rows = f.readlines()
    calcListLength = int(rows[0].strip())
    of = open(writeFile, "w")
    for i in range(1, calcListLength + 1):
        curRow = rows[i].split(" ")
        of.write("Case #{}: {}\n".format(i, testRange(int(curRow[0].strip()), int(curRow[1].strip()))))

def main():
    readFile(sys.argv[1], sys.argv[2])
    #print testRange(1, 4)
    #print testRange(10, 120)
    #print testRange(100, 1000)
    #print testRange(1000000, 100000000)
    #print testRangeTreading(1000000000, 10000000000)

if __name__ == '__main__':
    main()