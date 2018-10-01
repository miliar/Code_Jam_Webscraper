

def allRecPairs(someInt, minimum, maximum):
    stringRep = str(someInt)
    results = []
    for x in xrange(1, len(stringRep)):
        pairedInt = int(stringRep[x:]+stringRep[:x])
        if (pairedInt <= maximum) and (pairedInt >= minimum) and (someInt != pairedInt):
            results += [(someInt, pairedInt)]
    return results


def readCase(theFile):
    return theFile.readline().strip()

def writeCase(theFile, caseNumber, answer):
    theLine = "Case #%d: %s"%(caseNumber, answer)
    theFile.write(theLine + "\n")
    return

def solveCase(aLine):
    numbers = [int(x) for x in aLine.split()]
    minimum = numbers[0]
    maximum = numbers[1]
    sets = []
    for x in range(minimum, maximum+1):
        for pair in allRecPairs(x, minimum, maximum):
            if set(pair) not in sets:
                sets += [set(pair)]
    return str(len(sets))
                


def main(fileName):
    f = open(fileName, "U")
    g = open(fileName+".out", "w")
    cases = int(f.readline())
    for x in xrange(cases):
        writeCase(g, x+1, solveCase(readCase(f)))
    f.close()
    g.close()
    return

if __name__ == "__main__":
    from sys import argv
    main(argv[1])
