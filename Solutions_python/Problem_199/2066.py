import numpy as np
import queue

def vectorize(s):
    vector = np.zeros(len(s), dtype=np.bool)
    for i in range(len(s)):
        if s[i] == '+':
            vector[i] = 0
        else:
            vector[i] = 1
    return vector

def hash(arr):
    s = list()

    for e in arr:
        if e:
            s.append('-')
        else:
            s.append('+')
    return ''.join(s)


def flip(arr, s, e):
    arr[s:e] = np.ones(e-s) - arr[s:e]

def neighbors(arr, k):
    for i in range(0 ,arr.shape[0] - k+1):
        n = np.array(arr, copy=True)
        flip(n, i, i+k)
        yield n

def intersect(a, b):
    return not set(map(tuple, a)).isdisjoint(map(tuple, b))


def double_bfs(a, b, k):
    layerA = [a]
    layerB = [b]
    visitedA = set()
    visitedB  = set()
    visitedA.add(hash(a))
    visitedB.add(hash(b))
    counta = 0
    countb = 0

    i = 0
    while layerA and layerB and not intersect(layerA, layerB):
        if i % 2:
            tmpLayer = list()
            for e in layerA:
                for n in neighbors(e, k):
                    h = hash(n)
                    if h not in visitedA:
                        tmpLayer.append(n)
                        visitedA.add(h)
            layerA = list()
            layerA += tmpLayer
            counta += 1
        else:
            tmpLayer = list()
            for e in layerB:
                for n in neighbors(e, k):
                    h = hash(n)
                    if h not in visitedB:
                        tmpLayer.append(n)
                        visitedB.add(h)
            layerB = list()
            layerB += tmpLayer
            countb += 1
        i += 1

    if layerA and layerB:
        return counta + countb
    else:
        return -1




t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s, k = tuple(input().split(" "))
    k = int(k)
    r = double_bfs(vectorize(s), np.zeros(len(s)), k)
    if r == -1:
        r = 'IMPOSSIBLE'
    print("Case #{}: {} ".format(i, r))


