# Google Code Jam Contest
# @L01cDev
# Author: Loic Boyeldieu
# Date: 30-04-2017

import math

def getTopSurface(R):
    return R*R*math.pi

def getHeightSurface(R, H):
    return 2*R*H*math.pi

def getTotalSurface(R, H):
     return getTopSurface(R) + getHeightSurface(R, H)

def bestMeils(rayon,e, compare):
    if e[1]<=rayon:
        return 0
    r = getTotalSurface(e[1], e[2])
    if r > compare:
        return r
    return compare

T = int(raw_input())
for i in range(1, T + 1):
    N, K = [int(e) for e in raw_input().split(" ")]

    pancakes = []
    for j in range(N):
        idd = j
        R, H = [int(e) for e in raw_input().split(" ")]
        pancakes.append((idd, R, H))

    bestHeight = list(pancakes)
    bestHeight.sort(key= lambda x: getHeightSurface(x[1], x[2]), reverse=True)
    bestHeight = bestHeight[0:K]

    rayon = list(bestHeight)
    rayon.sort(key= lambda x: x[1], reverse=True)
    bestRayon = rayon[0][1]

    d = dict((x,(y,z)) for x,y,z in bestHeight)

    #best = list(pancakes)
    #best.sort(key= lambda x: getTotalSurface(x[1], x[2]), reverse=True)

    smallestHeightSurface = bestHeight[len(bestHeight)-1]
    sm = getHeightSurface(smallestHeightSurface[1], smallestHeightSurface[2])

    sol = list(pancakes)
    sol.sort(key= lambda x: (x[1], x[2]), reverse=True)

    result = 0
    for e in sol:
        if e not in d:
            if e[1]>bestRayon:
                if (getTotalSurface(e[1], e[2])-getTopSurface(bestRayon))>=sm:
                    result += getTotalSurface(e[1], e[2])
                    break
        
    if result>0:
        for e in bestHeight[0:K-1]:
            result += getHeightSurface(e[1], e[2])
    else:
        for e in bestHeight[0:K]:
            result += getHeightSurface(e[1], e[2])
        result += getTopSurface(bestRayon)

    print("Case #{}: {}".format(i, result))
