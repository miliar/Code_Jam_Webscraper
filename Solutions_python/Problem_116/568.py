#!/usr/bin/python
import os, sys, math

def processLine(line):
    # 1 = X
    # 2 = O
    canWin = 3
    #print line
    for x in line:
        if x == 'O':
            canWin = canWin & 2
        elif x == 'X':
            canWin = canWin & 1
        elif x == '.':
            return None
    if canWin == 0:
        return None
    if canWin == 1:
        return 'X won'
    return 'O won'

def processRow(case, i):
    return processLine(case[i])


def processCol(case, i):
    line = [x[i] for x in case]
    return processLine(line)


def solve(case):
    for i in range(4):
        val = processRow(case, i)
        if val:
            return val
        val = processCol(case, i)
        if val:
            return val
    val = processLine([case[0][0], case[1][1], case[2][2], case[3][3]])
    if val:
        return val
    val = processLine([case[0][3], case[1][2], case[2][1], case[3][0]])
    if val:
        return val
    for i in range(4):
        for j in range(4):
            if case[i][j] == '.':
                return 'Game has not completed'
    return 'Draw'

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        case = []
        for i in range(4):
            case.append(fileLines[index+i][:-1])
        # blank line
        index += 5
        answer = solve(case)
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
