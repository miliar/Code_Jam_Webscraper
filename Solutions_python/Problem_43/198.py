#!/usr/bin/python

import sys
from copy import copy

filename = sys.argv[1]

inputFile = open(filename, 'r')
outputFile = open('output.txt', 'w')
line = inputFile.readline()
line.rstrip('\n')

Trials = int(line)

def str2list(symStr):
    # be sure is stripped
    l = [symStr[i] for i in range(len(symStr))]
    return l

def getDict(symList):
    dict = {}
    dict[symList[0]] = 1
    cnt = 1
    putAZero = False
    for i in range(1,len(symList)):
        if not(dict.has_key(symList[i])):
            if not(putAZero):
                dict[symList[i]] = 0
                putAZero = True
            else:
                cnt = cnt + 1
                dict[symList[i]] = cnt
    return dict

def symStr2NumAndBase(symStr):
    rng = len(symStr)
    symList = str2list(symStr)
    D = getDict(symList)
    for i in range(rng):
        symList[i] = D[symList[i]]
    return (symList, len(D.keys()))

def list2string(numList):
    return ''.join(map((lambda x: str(x)), numList))

'''
def numTuple2Dec(tuple):
    if tuple[1] == 1:
        b = 2
    else:
        b = tuple[1]
    return int(list2string(tuple[0]), b)
'''

def powerList(tuple):
    power = copy(tuple[0])
    if tuple[1] == 1:
        base = 2
    else:
        base = tuple[1]
    rng = len(power)
    for i in range(rng):
        power[rng - i - 1] = pow(base,i)
    return power

def numTuple2Dec(tuple):
    nL = tuple[0]
    pL = powerList(tuple)
    return sum([nL[i]*pL[i] for i in range(len(pL))])

for i in range(Trials):
    line = inputFile.readline()
    tuple = symStr2NumAndBase(line.rstrip(' \n'))
    decNum = numTuple2Dec(tuple)
    outputFile.write('Case #' + str(i+1) + ': ' + str(decNum) + '\n')

inputFile.close()
outputFile.close()
