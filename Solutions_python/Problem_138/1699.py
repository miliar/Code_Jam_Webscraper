def main():
    numOfIter = int(raw_input())
    for i in xrange(numOfIter):
        (firstSet, secondSet, iterations) = parseData()
        warR = war(firstSet[:], secondSet[:], iterations)
        decR = dec(firstSet[:], secondSet[:], iterations)
        print "Case #%d: %d %d" % (i + 1, decR, warR)

def war(firstSet, secondSet, iterations):
    score = 0
    for i in xrange(iterations):
        elem = firstSet[i]
        minGT = 1
        for otherElem in secondSet:
            if otherElem > elem and otherElem < minGT:
                minGT = otherElem
        if minGT == 1:
            for otherElem in secondSet:
                if otherElem < minGT:
                    minGT = otherElem
            score += 1
        secondSet.remove(minGT)
    return score

def dec(firstSet, secondSet, iterations):
    score = 0
    for i in xrange(iterations):
        #print i, firstSet, secondSet
        firstMax = max(firstSet)
        secondMax = max(secondSet)
        if firstMax > secondMax:
            score += 1
            firstSet.remove(firstMax)
            secondSet.remove(secondMax)
            continue

        firstMin = min(firstSet)
        firstSet.remove(firstMin)
        secondSet.remove(secondMax)
    return score


def parseData():
    iterations = int(raw_input())
    firstSet = [float(x) for x in raw_input().split(" ")]
    secondSet = [float(x) for x in raw_input().split(" ")]
    return (firstSet,secondSet,iterations)

if __name__ == "__main__":
    main()
