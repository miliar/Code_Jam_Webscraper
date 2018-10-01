import sys

def getNumSwitches(enginesList, queries):
    numEngines = len(enginesList)

    switches = [0]*numEngines
    
    enginesHash = {}
    for i, engine in enumerate(enginesList):
        enginesHash[engine] = i

    switches[enginesHash[queries[0]]] = None

    for query in queries[1:]:
        engineIdx = enginesHash[query]
        
        minPrevSwitches = minNonNone(switches)

        for i in range(numEngines):
            if switches[i] is not None:
                switches[i] = min(minPrevSwitches + 1, switches[i])
            else:
                switches[i] = minPrevSwitches + 1

        switches[engineIdx] = None

    return minNonNone(switches)

def minNonNone(arr):
    min = None
    for val in arr:
        if val is None:
            continue
        else:
            if min is None or min > val:
                min = val

    assert min is not None    

    return min


inFile = sys.stdin
#inFile = open("A-small-attempt1.in", 'r')

numCases = int(inFile.readline())
for caseNum in range(numCases):
    enginesList = []
    queries = []    

    numEngines = int(inFile.readline())
    for i in range(numEngines):
        enginesList.append(inFile.readline())

    numQueries = int(inFile.readline())
    for i in range(numQueries):
        queries.append(inFile.readline())

    if numQueries == 0:
        print "Case #%d: 0" % (caseNum + 1)
        continue
    
    numSwitches = getNumSwitches(enginesList, queries)
    print "Case #%d: %d" % (caseNum + 1, numSwitches)
