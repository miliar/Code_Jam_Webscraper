#!/usr/bin/python
import os, sys, math

def solve(case):
    possibles = set(case[0]['board'][case[0]['guess']])
    possibles = list(possibles.intersection(set(case[1]['board'][case[1]['guess']])))
    if len(possibles) == 1:
        return possibles[0]
    if len(possibles) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

def main(filename):
    fileLines = open(filename, 'r').readlines()
    index = 0
    numCases = int(fileLines[index][:-1])
    index += 1
    for caseNum in range(numCases):
        case = []
        for i in range(2):
            curCase = {}
            curCase['guess'] = int(fileLines[index][:-1]) - 1
            index += 1
            curCase['board'] = []
            for j in range(4):
                curCase['board'].append(fileLines[index+j][:-1].split(' '))
            index += 4
            case.append(curCase)
        answer = solve(case)
        #print caseStr
        print "Case #%d: %s" % (caseNum + 1, answer)

if __name__ == '__main__':
    main(sys.argv[1])
