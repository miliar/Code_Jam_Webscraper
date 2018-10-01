import sys
import math
from math import pi

def getCir(radius):
    return pi *2*radius

def getSArea(radius, height):
    return getCir(radius) * height

def getArea(radius):
    return radius * radius * pi

def getInts():
    return list(map(int, input().split(" ")))

def getFloats():
    return list(map(float, input().split(" ")))

def getNLine( fnc, n ):
    return [ fnc() for y in range(n) ]

def solve(n, k, cakes):
    cakes.sort(key=lambda x:x[0],reverse = True)
    maxA = 0
    for i in range(0,n-k+1):
        maxA = max(maxA, getArea(cakes[i][0])+getSArea(cakes[i][0],cakes[i][1])+cakeMax(k-1,cakes[i+1:]));

    return maxA

def cakeMax(k, cakes):
    cakeArea = [getSArea(c[0],c[1]) for c in cakes]

    cakeArea.sort(reverse = True);
    return sum(cakeArea[:k]);


T = int(input())
for i in range(T):
    [n, k] = getInts()
    cakes = getNLine(getFloats,n)
    print('Case #{}: {:.9f}'.format(i + 1, solve(n,k,cakes)))
