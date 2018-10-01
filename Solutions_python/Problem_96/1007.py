#!/usr/bin/env python2
import sys
import math

class Test:
    pass
class Result:
    pass


def parseInput(path):
    ret = []
    testFile = open(path)
    inputSize = int(testFile.readline())

    for i in range(inputSize):
        text = testFile.readline().split()
        test = Test()
        googlerCount = int(text[0])
        test.sCount = int(text[1])
        test.minScore = int(text[2])
        test.scores = []
        for j in range(googlerCount):
            test.scores.append(int(text[3+j]))

        ret.append(test)

    return ret

def solve(test):
    maxGooglers = 0

    #Check the scores that absolutely are higher
    #That would be those greater (minBestScore-1)*3
    tempScores = test.scores
    possibleSurprises = []
    for score in tempScores:
        if (test.minScore-1) * 3 >= score:
            possibleSurprises.append(score)
        else:
            maxGooglers += 1

    #Check the scores that need to be surprising
    surprisesLeft = test.sCount
    for score in possibleSurprises:
        if surprisesLeft == 0:
            break
        elif score <=1: #A score of 1 can't be surprising
            continue
        elif test.minScore * 3 - 4 <= score:
            surprisesLeft -= 1
            maxGooglers += 1

    return maxGooglers



tests = parseInput(sys.argv[1])
results = []
for test in tests:
    results.append(solve(test))

for i in range(len(results)):
    print "Case #{0}: {1}".format(i+1, results[i])