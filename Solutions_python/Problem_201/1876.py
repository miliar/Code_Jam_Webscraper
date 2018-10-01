#file read operation
t = int(raw_input()) # number of Input

#max(Ls,Rs) min(Ls,Rs)
def maxMin(posDict, pos):
    Ls = 0
    i = pos - 1
    for i in range(pos-1, -1, -1):
        if space[i] == 'o':
            break
    Ls = pos - i - 1
    Rs = 0
    i = pos + 1
    for i in range(pos+1, len(space)):
        if space[i] == 'o':
            break
    Rs = i - pos - 1
    return max(Ls, Rs), min(Ls, Rs)

#which position to occupy
def occupy(posDict, N):
    minV = -1
    minList = []
    maxList = []
    posList = []
    for i in range(1, N+1):
        if i in posDict:
            L, R = posDict[i]
            Ls = i - L - 1
            Rs = R - i - 1
            maxS,minS = max(Ls, Rs), min(Ls, Rs)
            if minS > minV:
                minList = [minS]
                maxList = [maxS]
                posList = [i]
                minV = minS
            elif minS == minV:
                minList.append(minS)
                maxList.append(maxS)
                posList.append(i)
    if len(minList) == 1:
        return posList[0]
    else:
        maxAll = max(maxList)
        return posList[maxList.index(maxAll)]

def getposDict(N):
    posDict = {}
    for i in range(1, N+1):
        posDict[i] = [0,N+1]
    return posDict

def updatePosDict(posDict, pos):
    del posDict[pos]
    for p in posDict.keys():
        L,R = posDict[p]
        if p < pos < R:
            R = pos
        elif L < pos < p:
            L = pos
        posDict[p] = [L,R]

def solve(N, K):
    posDict = getposDict(N)
    for i in range(K-1):
        pos = occupy(posDict, N)
        updatePosDict(posDict, pos)
    pos = occupy(posDict, N)
    L,R = posDict[pos]
    Ls = pos - L - 1
    Rs = R - pos - 1
    return max(Ls, Rs), min(Ls, Rs)

for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    N, K = int(line[0].strip()), int(line[1].strip())
    maxS, minS = solve(N, K)
    print "Case #{}: {} {}".format(i, maxS, minS)
