'''
Created on 03-May-2014

@author: Pankaj
'''
import os, sys

def getTestCases(numCases, casesData):
    cases = list()
    for eachCase in casesData:
        cases.append(eachCase[:-1].split(" "))
    return cases

def getResult(resultData):
    def writeResult(fh, caseNum, caseResult):
        fh.write("Case #%d: %s\n" % (caseNum, caseResult))
    
    outFile = os.path.splitext(inFile)[0] + ".out"
    fh = file(outFile, "w")
    for i, caseResult in enumerate(resultData):
        writeResult(fh, i+1, caseResult)

def resolveCase(testData):
    slotA, slotB, lot = int(testData[0]), int(testData[1]), int(testData[2])
    chances = 0
#     print
#     print slotA, slotB, lot
    for a in range(slotA):
        for b in range(slotB):
#             print a, "{0:b}".format(a)
#             print b, "{0:b}".format(b)
#             print a&b, "{0:b}".format(a&b)

            if a&b < lot:
#                 print "gotcha"
                chances += 1
    return str(chances)

inFile = sys.argv[1] 
fh = file(inFile, "r")
fileData = fh.readlines()
fh.close()

numCases = int(fileData[0][:-1])
testCases = getTestCases(numCases, fileData[1:])

testResults = list()
for eachCase in testCases:
    testResults.append(resolveCase(eachCase))

getResult(testResults)

