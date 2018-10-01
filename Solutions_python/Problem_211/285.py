#!/usr/bin/python
import sys
import operator as op
from itertools import combinations
from functools import reduce
class AttDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

def getProb(probabilities, minCores):
    prob = 0
    indices = set(range(len(probabilities)))
    for i in range(minCores, len(probabilities) + 1):
        for c in combinations(indices, i):
            prob += reduce(op.mul, [probabilities[int(x)] for x in c]) * reduce(op.mul, [1-probabilities[int(x)] for x in indices - set(c)], 1)
    return prob

def processCase(case, caseNum):
    # the n highest => try to get them to the same number (lowest first)
    case.probabilities.sort(reverse=1)
    important = case.probabilities[:case.minCores]
    others = case.probabilities[case.minCores:]
    leftover = case.numUnits
    if case.minCores is 1:
        add = min(leftover, 1 - important[0])
        important[0] += add
        leftover -= add
    else:
        while leftover > 0:
            higher = 0
            sameAmount = 1
            for x in reversed(important[:-1]):
                if x > important[-1]:
                    higher = x
                    break
                sameAmount += 1
            if not higher:
                break
            add = min(leftover, (higher - important[-1]) * sameAmount)
            for x in range(len(important) - sameAmount, len(important)):
                important[x] += add / sameAmount
            leftover -= add
            important.sort(reverse=1)
        add = min(leftover, len(important) * (1 - important[0]))
        for x in range(len(important)):
            important[x] += add / len(important)
        leftover -= add
    if len(others) > 1:
        while leftover > 0:
            higher = 0
            sameAmount = 1
            for x in reversed(others[:-1]):
                if x > others[-1]:
                    higher = x
                    break
                sameAmount += 1
            if not higher:
                break
            add = min(leftover, (higher - others[-1]) * sameAmount)
            for x in range(len(others) - sameAmount, len(others)):
                others[x] += add / sameAmount
            leftover -= add
            others.sort(reverse=1)
        add = min(leftover, len(others) * (1 - others[0]))
        for x in range(len(others)):
            others[x] += add / len(others)
        leftover -= add
    else:
        if len(others):
            others[0] += leftover
            others[0] = min(others[0], 1)

    print("Case #%d: %.6f" % (caseNum, getProb(important + others, case.minCores)))

with open(sys.argv[1]) as f:
    data = f.read().split('\n')
    i = 0
    testCaseNum = int(data[i])
    i += 1
    testCases = []
    for _ in range(testCaseNum):
        coreNum, minCores = [int(x) for x in data[i].split(' ')]
        i += 1
        numUnits = float(data[i])
        i += 1
        probabilities = [float(x) for x in data[i].split(' ')]
        i += 1
        dic = AttDict()
        dic.coreNum = coreNum
        dic.minCores = minCores
        dic.numUnits = numUnits
        dic.probabilities = probabilities
        testCases.append(dic)
    num = 0
    for case in testCases:
        num += 1
        processCase(case, num)
