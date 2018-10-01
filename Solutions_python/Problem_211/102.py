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
    U = readValue(float)

    probs = readValues(float)

    return N, K, U, probs


def solve(N, K, U, probs):
    EPS = 0.000000000000001
    best = 0
    l, r = 0, 1
    while r - l > EPS:
        mid = (l + r) / 2

        needed = 0
        totalProb = 1
        for prob in probs:
            if prob < mid:
                needed += mid - prob
                totalProb *= mid
            else:
                totalProb *= prob

        if needed <= U:
            l = mid + EPS
            best = max(best, totalProb)
        else:
            r = mid - EPS

    return best


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
