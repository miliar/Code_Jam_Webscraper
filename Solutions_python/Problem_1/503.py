#!/usr/bin/python
#Paul Ringstad
#2008

import os
import sys
import copy

sys.setrecursionlimit(1500)

#scores are good when low
bestScore = 1000
bestMoves = []
bestMemo = []

def findBestRoute(curMoves, score, idx, se, qs):
    global bestScore
    global bestMoves
    global bestMemo

    #base case
    if idx >= len(qs):
        if score < bestScore :
            bestScore = int(score)
            bestMoves = copy.copy(curMoves)
        return

    #no point in continuing if we've switched too many times    
    if score > bestMemo[idx]:
        return
    else:
        bestMemo[idx] = int(score)

    #if the query is the same as the current server
    if curMoves[-1] == qs[idx]:

        #switch to one of the other servers
        for name in se:
            if name != qs[idx]:
                curMoves.append(name)
                findBestRoute(curMoves, score + 1, idx + 1, se, qs)
                curMoves.pop()
    else:
        curMoves.append(curMoves[-1])
        findBestRoute(curMoves, score, idx + 1, se, qs)
        curMoves.pop()


#
#
#
#
#Here's where the magic begins!
f = open(sys.argv[1])

numCases = int(f.readline())
  
i=1
while numCases > 0:
    bestScore = 1000
    bestMoves = []
    bestMemo = []

    se = []
    qs = []
    
    #Get all data from file
    numSe = int(f.readline())
    
    while numSe > 0:
        se.append(f.readline().strip())
        numSe = numSe - 1

    numQs = int(f.readline())
    
    #init the memoized scores
    j = 0
    while j < numQs:
        bestMemo.append(bestScore)
        j = j + 1

    if( numQs == 0 ):
        bestScore = 0
    else:
        while numQs > 0:
            qs.append(f.readline().strip())
            numQs = numQs - 1

        for name in se:
            if( name != qs[0] ):
                findBestRoute([name], 0, 1, se, qs)

    print "Case #" + str(i) + ": " + str(bestScore)
 
    numCases = numCases - 1
    i = i + 1


