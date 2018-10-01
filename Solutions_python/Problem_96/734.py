from math import ceil

def canGetGTp(closestScores, S, p):
    """
    #print closestScores, S, p
    bestNum = -1
    for a in range(len(closestScores)):
        x = closestScores[a]
        diff = abs(x - p)
        closestToX = -1
        best = -1
        other = -2
        for n in range(len(closestScores)):
            cur = abs(closestScores[n] - (closestScores[a] + diff))
            if n != a and (best == -1 or cur < best):
                best = cur
                other = closestToX
                closestToX = n
            elif closestToX != -1:
                other = n
        newOnes = [x + diff, closestScores[closestToX] - diff, closestScores[other]]
        if newOnes[1] < 0:
            newOnes[2] += newOnes[1]
            newOnes[1] = 0
        numDifferences = 0
        numSurprising = 0
        lessThanZero = False
        #print "current: ", a, closestToX, other, closestScores[a], closestScores[closestToX], closestScores[other], newOnes
        for b in range(len(newOnes)):
            if newOnes[b] < 0:
                lessThanZero = True
                break
            for c in range(b, len(newOnes)):
                if abs(newOnes[b] - newOnes[c]) > 2:
                    #print newOnes[b], newOnes[c], b, c
                    numDifferences += 1
                elif abs(newOnes[b] - newOnes[c]) == 2:
                    #print newOnes[b], newOnes[c], b, c
                    numSurprising += 1
        #print numDifferences
        if not lessThanZero and numDifferences == 0 and numSurprising <= S:
            if (bestNum == -1 or numSurprising < bestNum):
                bestNum = numSurprising
    if (bestNum == -1):
        return False, 0
    else:
        return True, bestNum
    """
def canGetGTp(closestScores, S, p):
    for cur in range(len(closestScores)):
        x = closestScores[cur]
        diff = p - x
        if diff >= 2:
            continue
        next1 = (cur + 1) % len(closestScores)
        next2 = (next1 + 1) % len(closestScores)
        f = closestScores[cur]
        s = closestScores[next1]
        t = closestScores[next2]
        a = f + diff
        b = s - diff
        c = t
        if b < 0:
            c += b
            b = 0
        if c < 0:
            continue
        d1 = abs(a - b)
        d2 = abs(b - c)
        d3 = abs(a - c)
        #print d1, d2, d3, cur, next1, next2, f, s, t
        #print "ABC: ", a, b, c
        if d1 > 2 or d2 > 2 or d3 > 2:
            continue
        numS = 0
        if d1 == 2 or d2 == 2 or d3 == 2:
            numS += 1
        if numS <= S:
            #print "<<", f, s, t
            return True, numS
    return False, 0

def getClosestScores(googler):
    out = []
    if googler%3 == 0:
        return [googler/3, googler/3, googler/3]
    else:
        d = int(round(googler/3.0))
        a = 0
        if d == int(ceil(googler/3.0)):
            a = -1
        else:
            a = 1
        f = d
        f += a
        if (f < d):
            return [f, d, d]
        else:
            return [d, d, f]

T = int(raw_input())
for abc in range(T):
    line = [int(x) for x in raw_input().split()]
    N = line[0]
    S = line[1]
    p = line[2]
    googlers = line[3:]
    #print "Case #" + str(abc+1) + ":"
    closestScores = []
    for googler in googlers:
        # get closest scores which add to googler, then 
        # use S and stuff to maximize # with max score > p
        closestScores.append(getClosestScores(googler))
        #print googler, closestScores[-1]

    total = 0
    for x in range(len(googlers)):
        containsGTp = max(closestScores[x]) >= p
        if containsGTp:
            total+=1
        else:
            res = canGetGTp(closestScores[x], S, p)
            if (res[0]):
                total += 1
                S -= res[1]
    print "Case #" + str(abc + 1) + ": " + str(total)
