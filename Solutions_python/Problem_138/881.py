prefix = "D-large"
postfixIn = ".in"
postfixOut = ".out"

fileIn = open(prefix + postfixIn, "r")
lines = fileIn.readlines()
fileIn.close()

results = []
template = "Case #%d: %d %d\n"

############################################################

casesCount = int(lines[0].strip())
for i in xrange(casesCount):
    deceitfulScore = 0
    originalScore = 0
    blocksCount = int(lines[3 * i + 1].strip())
    naomiBlocks = [float(elem) for elem in lines[3 * i + 2].strip().split()]
    kenBlocks = [float(elem) for elem in lines[3 * i + 3].strip().split()]
    naomiBlocks.sort()
    kenBlocks.sort()

    naomiBlocksDeceitful = naomiBlocks[:]
    kenBlocksDeceitful = kenBlocks[:]
    stack = []
    while len(naomiBlocksDeceitful) > 0 or len(kenBlocksDeceitful) > 0:
        if len(naomiBlocksDeceitful) == 0:
            break
        elif len(kenBlocksDeceitful) == 0:
            deceitfulScore += len(naomiBlocksDeceitful)
            break
        else:
            if naomiBlocksDeceitful[0] < kenBlocksDeceitful[0]:
                if len(stack) > 0:
                    stack.pop()
                    deceitfulScore += 1
                naomiBlocksDeceitful = naomiBlocksDeceitful[1:]
            else:
                stack.append(kenBlocksDeceitful[0])
                kenBlocksDeceitful = kenBlocksDeceitful[1:]

    naomiBlocksOrg = naomiBlocks[:]
    kenBlocksOrg = kenBlocks[:]
    for naomiBlocksOrg in naomiBlocks:
        kenBlockMax = max(kenBlocksOrg)
        if kenBlockMax < naomiBlocksOrg:
            originalScore += 1
            kenBlocksOrg.remove(kenBlocksOrg[0])
        else:
            for kenbBlock in kenBlocksOrg:
                if kenbBlock > naomiBlocksOrg:
                    kenBlocksOrg.remove(kenbBlock)
                    break

    result = template % (i + 1, deceitfulScore, originalScore)
    results.append(result)

############################################################

fileOut = open(prefix + postfixOut, "w")
for result in results:
    fileOut.write(result)
fileOut.close()
