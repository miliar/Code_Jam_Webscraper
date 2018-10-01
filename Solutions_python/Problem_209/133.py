#!/usr/bin/env python3
import math, collections, itertools
from sys import stdin


def readValue(valueType):
    return valueType(stdin.readline())


def readValues(valueType):
    return list(map(valueType, stdin.readline().split()))


class Mouth():
    count = 1

    @classmethod
    def answer(cls, answer):
        print("Case #{}: {}".format(cls.count, answer))
        cls.count += 1


def readInput():
    N, K = readValues(int)
    pies = []
    for _ in range(N):
        pies.append(readValues(int))

    return N, K, pies


def solve(N, K, pies):
    pies.sort(key=lambda x: -x[0])
    
    best = [math.pi * R * R + 2 * math.pi * R * H for R, H in pies]
    for k in range(1, K):
        bestSoFar = best[k-1], k-1

        for i in range(k, N):
            tmp = best[i]

            best[i] = bestSoFar[0]\
                + 2 * math.pi * pies[i][0] * pies[i][1]

            if tmp > bestSoFar[0]:
                bestSoFar = tmp, i

    return max(best)


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
