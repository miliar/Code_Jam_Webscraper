import sys

def buildLetterPos(line):

    letterPos = dict()
    for i in range(len(line)):
        letter = line[i]
        if letter not in letterPos:
            letterPos[letter] = list()
        letterPos[letter].append(i)

    return letterPos

def travelScater(curScater, tLeftBound, tIdx, tLine, endLen):
    if tIdx >= endLen:
        return 1

    tLetter = tLine[tIdx]
    if len(curScater[tLetter]) == 0:
        return 0

    result = 0

    buck = list()
    while len(curScater[tLetter]) > 0:
        cLeftBound = curScater[tLetter].pop(0)
        buck.append(cLeftBound)
        if cLeftBound >= tLeftBound:
            result += travelScater(curScater, cLeftBound, tIdx+1, tLine, endLen)
    curScater[tLetter] = buck

    return result


if __name__ == '__main__':
    inputLines = open(sys.argv[1], 'r').read().strip().split('\n')
    testCaseNo = int(inputLines.pop(0))
    outFP = open(sys.argv[1]+'.out.txt', 'w')

    caseNo = 1
    welcomeCodeJam = 'welcome to code jam'
    welComeSet = set(welcomeCodeJam)
    welcomeCodeJamLen = len(welcomeCodeJam)

    for line in inputLines:
        tScater = buildLetterPos(line)
        if not welComeSet <= set(line):
            output = 'Case #%i: %04i'%(caseNo, 0)
        else:
            output = 'Case #%i: %04i'%(caseNo, travelScater(tScater, -1, 0, welcomeCodeJam, welcomeCodeJamLen))
        print output
        outFP.write(output+'\n')
        caseNo += 1


