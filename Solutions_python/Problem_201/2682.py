import fileinput

def placeNext(state):
    minVal = 0
    maxVal = 0
    coords = -1
    lastFullLeft = 0
    i = 0
    while i < len(state):
        if state[i]:
            i += 1
            continue
        lastFullLeft = i-1
        while state[i] == False:
            i += 1
        lastFullRight = i
        optimalLocation = (lastFullRight + lastFullLeft)/2
        deltaL = optimalLocation - lastFullLeft - 1
        deltaR = lastFullRight - optimalLocation - 1
        if minVal < min(deltaL,deltaR) or minVal == min(deltaL,deltaR) and maxVal < max(deltaL,deltaR) or coords == -1:
            coords = optimalLocation
            minVal = min(deltaL,deltaR)
            maxVal = max(deltaL,deltaR)
    assert coords > 0
    state[coords] = True
    return minVal,maxVal

def solveBruteForce(N,K):
    stallState = [True]+[False]*N+[True]
    minVal = 0
    maxVal = 0
    for i in range(K):
        minVal,maxVal = placeNext(stallState)
    return str(maxVal)+" "+str(minVal)

def main():
    it = fileinput.input()
    it.next()
    for i,l in enumerate(it):
        N,K = l.split()
        N,K = int(N),int(K)
        print  "Case #%d: %s" % ( i+1, solveBruteForce(N,K))

if __name__ == "__main__":
    main()
