#!/usr/bin/env python2




def getProblemMote(size, motes) :
    for mote in motes :
        if size <= mote :
            return (size,mote)
        size = size + mote
    return None

def isSolvable(size, motes) :
    if len(motes) == 0 :
        return True
    last = motes[-1]
    for mote in motes :
        if size <= mote :
            return False
        if size > last :
            return True
        size = size + mote
    return True


def dropMote(motes) :
    motes = motes[:]
    motes.pop()
    return motes

def addMote(mote, motes) :
    motes = motes[:]
    motes.append(mote)
    motes.sort()
    return motes


def getSubStates(size, motes) :
    problem = getProblemMote(size, motes)
    less = dropMote(motes)
    if (problem[0] < 2) :
        return [less]
    more = addMote(problem[0]-1, motes)
    return [less,more]


def countChangesNeeded(size, motes) :
    if isSolvable(size, motes) :
        return 0
    states = [motes]
    deviations = 1
    while True :
        newstates = []
        for state in states :
            newstates = newstates + getSubStates(size, state)
        for state in newstates :
            if isSolvable(size, state) :
                return deviations
        states = newstates
        deviations += 1



T = int(raw_input())

for t in xrange(T) :
    size = int(raw_input().split()[0])
    motes = sorted([int(m) for m in raw_input().split()])
    print "Case #" + `t+1` + ": " + `countChangesNeeded(size, motes)`
