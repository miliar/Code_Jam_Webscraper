# <beyer.andrew@gmail.com>
import sys

inputFile = open(sys.argv[1])

def ReadStrLine():
    return inputFile.readline().rstrip("\r\n")

def ReadIntLine():
    return int(inputFile.readline().rstrip("\r\n"))

def Step(query, prev):
    next = []
    for x in range(len(prev)):
        if prev[x]>=0:
            next.append(prev[x]+1)
        else:
            next.append(-1)
    next[query] = 0
    return next

def DoCase():
    engineCount = ReadIntLine()
    engines = {}
    for e in range(engineCount):
        engines[ReadStrLine()] = e

    queryCount = ReadIntLine()
    queries = []
    for x in range(queryCount):
        queries.append(engines[ReadStrLine()])

    nextUses = []
    prev = [-1]*engineCount
    for query in reversed(queries):
        nextUses.insert(0,Step(query,prev))
        prev = nextUses[0]

    switches = 0
    i = 0 
    while i < queryCount-1:
        if min(nextUses[i]) < 0:
            return switches
        else:
            switches += 1
            i += max(nextUses[i])
    return switches

caseCount = ReadIntLine()
for case in range(1, caseCount+1):
    print "Case #%d:" % case, DoCase()
