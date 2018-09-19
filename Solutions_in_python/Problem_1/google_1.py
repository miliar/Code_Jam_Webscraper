import sys

f = open(sys.argv[1])
nbCases = int(f.readline())
for idxCase in xrange(nbCases):
    nbSearchEngines = int(f.readline())
    allSearchEngines = set()
    for _ in xrange(nbSearchEngines):
        name = f.readline()
        allSearchEngines.add(name) 
    currentSearchEngines = allSearchEngines.copy()
    nbRequests = int(f.readline())
    nbChanges = 0
    for _ in xrange(nbRequests):
        request = f.readline()
        currentSearchEngines.discard(request)
        if not currentSearchEngines:
            nbChanges += 1
            currentSearchEngines = allSearchEngines.copy()
            currentSearchEngines.discard(request)
    print "Case #%d: %d"%(idxCase+1, nbChanges)

