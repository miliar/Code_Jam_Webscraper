'''
Created on 08.05.2010

@author: Dong Li
'''
import os.path
import string

existingPaths = []
toAddPaths = []

def getResult():
    existingPathsSet = set(existingPaths)
    toAddPathsSet = set(toAddPaths)
    diffSet = toAddPathsSet - existingPathsSet
    return len(diffSet)

def collectPaths(paths, line):
    while string.rfind(line, "/") != -1 and string.rfind(line, "/") != 1:
        paths.append(string.strip(line))
        line = line[:string.rfind(line, "/")]

largeFile = "A-large.in"
smallFile = "A-small-attempt0.in"
inputFile = ""
if  os.path.exists(largeFile):
    inputFile = largeFile
else:
    inputFile = smallFile
outputFile = open(inputFile.split(".")[0] + ".out", 'w')
input = open(inputFile)

N = 0
M = 0
caseNum = 0
lineCount = 0
inCase = False
caseCount = 0
count = 0
for line in input:
    if count == 0:
        caseNum = int(line)
        count += 1
    else:
        if not inCase:
            N = int(line.split()[0])
            M = int(line.split()[1])
            lineCount = 1
            caseCount += 1
            inCase = True
            existingPaths = []
            toAddPaths = []
        elif inCase and lineCount <= N:
            collectPaths(existingPaths, line)
            lineCount += 1
        elif inCase and lineCount > N and lineCount <= N + M:
            collectPaths(toAddPaths, line)
            if lineCount == N + M:
                inCase = False
                result = "Case #" + str(caseCount) + ": " + str(getResult())
                print result
                outputFile.write(result + "\n")
            lineCount += 1

input.close()
outputFile.close()










