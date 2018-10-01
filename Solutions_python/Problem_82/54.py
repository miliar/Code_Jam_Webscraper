

def isDone(d, dists):
    return all(x >= d for x in dists)

def inRange(dists, i):
    return i >= 0 and i < len(dists)

def stepEnd(d, dists, start, sign):
    dists[start] += 1
    return start
"""
    i = start
    while True:
        if not inRange(dists, i):
            return start
        if dists[i] < d:
            break
        i += sign
    dists[i] += 1
    return i
"""
def stepDists(d, dists):
    lowChange = stepEnd(d, dists, 0, 1)
    highChange = stepEnd(d, dists, len(dists) - 1, -1)
    for i in range(lowChange, highChange):
        if dists[i] < d and dists[i + 1] >= d:
            dists[i] += 1
            dists[i + 1] -= 1
        elif dists[i] > d and dists[i + 1] <= d:
            dists[i] -= 1
            dists[i + 1] += 1

def getNumSteps(d, dists):
    #print dists
    steps = 0
    while not isDone(d, dists):
        stepDists(d, dists)
        #print dists
        steps += 1
    return steps
    
def main():
    numCases = int(raw_input())
    for case in range(numCases):
        line = raw_input().split(' ')
        c = int(line[0])
        d = int(line[1])
        dists = []
        prevPos = None
        for i in range(c):
            line = raw_input().split(' ')
            p = int(line[0])
            v = int(line[1])
            if prevPos != None:
                dists.append(2 * (p - prevPos))
            prevPos = p
            for j in range(v - 1):
                dists.append(0)
        steps = float(getNumSteps(2 * d, dists)) / 2
        print "Case #%d: %f" % (case + 1, steps)
                
            

main()
    
