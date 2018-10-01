import sys

# stalls is an array of booleans, True means someone is standing there
def addPerson(stalls):
    longestChain, longestChainLoc, currentChain = 0, 0, 0
    for i in range(len(stalls)):
        if stalls[i]:
            if currentChain > longestChain:
                longestChain = currentChain
                longestChainLoc = i - 1 #  right end of longest chain
            currentChain = 0
        else:
            currentChain += 1            
            
    minDist = (longestChain - 1) / 2
    maxDist = (longestChain -1) - minDist
    stalls[longestChainLoc - maxDist] = True
    return stalls, maxDist, minDist

def getLRS(N, K):
    stalls = [True] + [False]*N + [True]
    for i in range(K):
        stalls, maxDist, minDist = addPerson(stalls)
    return maxDist, minDist

if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname) as f:
        content = f.readlines()
        i = 1
        for test in content[1:]:
            n, k = test.split()
            result = getLRS(int(n), int(k))
            print 'Case #%d: %d %d' % (i, result[0], result[1])
            i += 1
