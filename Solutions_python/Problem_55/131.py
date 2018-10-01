
#
# Google Code Jam 2010
# Qualification Round: C. Theme Park
# submission by EnTerr
#

import sys

f = open(sys.argv[1])
def input(): return f.readline().strip();

def runNextRide(state):
    # given <state>, return (<earnings>, <state>) after the run
    freeSpace = maxLoad
    while groups[state] <= freeSpace:
        freeSpace -= groups[state]
        state += 1
        if state >= numGroups: state = 0
    return (maxLoad - freeSpace, state)

for caseNo in xrange(1, int(input())+1):
    (numRuns, maxLoad, numGroups) = map(int, input().split())
    groups = map(int, input().split())
    assert(len(groups) == numGroups)
    maxLoad = min(maxLoad, sum(groups)) # can load every group at most once per run

    # determine the loop
    trail = {} # trail[state] = (numRunsToReachThis, totalEarningsUpToNow)
    state, earnings, n = 0, 0, 0
    while state not in trail:
        trail[state] = (n, earnings)
        (revenue, state) = runNextRide(state)
        earnings += revenue
        n += 1
    prologLength = trail[state][0]
    prologRevenue = trail[state][1]
    loopStart = state
    loopLength = n - prologLength
    loopRevenue = earnings - prologRevenue

    state, earnings = 0, 0    
    if numRuns >= prologLength:
        numRuns -= prologLength
        earnings += prologRevenue
        state = loopStart
        numLoops = numRuns / loopLength
        numRuns -= numLoops * loopLength
        earnings += numLoops * loopRevenue
    # process the 'epilog', not complete loops
    for _ in xrange(numRuns):
        (revenue, state) = runNextRide(state)
        earnings += revenue
            
    print 'Case #%d: %d' % (caseNo, earnings)

