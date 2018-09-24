
import string

numEngines = 0
engines = {}
numSearches = 0
searches = []

def readInput():
    global numEngines
    global numSearches
    global engines
    global searches
    f = open("large.in")
    testCases = int(f.readline())
    for counter in range(testCases):
        numEngines = int(f.readline())
        engines = {}
        for j in range(numEngines):
            engines[string.strip(f.readline())] = j
        numSearches = int(string.strip(f.readline()))
        searches = []
        for j in range(numSearches):
            searches.insert(j, string.strip(f.readline()))
        result = "Case #" + str(counter+1) + ": "
        result += str(solve())
        print result
        

def solve():
    global searches
    global numSearches
    global numEngines
    i = 0
    switch = 0
    used = {}
    while (i < numSearches):
        used[engines[searches[i]]] = 1
        if (len(used) == numEngines):
            used = {}
            used[engines[searches[i]]] = 1
            switch += 1
        i += 1
    return switch

readInput()
