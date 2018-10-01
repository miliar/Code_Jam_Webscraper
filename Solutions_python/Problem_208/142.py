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
    N, Q = readValues(int)
    horses = []
    for _ in range(N):
        horses.append(readValues(int))
    dist = []
    for _ in range(N):
        dist.append(readValues(int))
    routes = []
    for _ in range(Q):
        routes.append(readValues(int))
    return N, horses, dist, routes


def solve(N, horses, dist, routes):
    best = [-1] * N
    best[0] = 0
    for i in range(N-1):
        soFar = 0
        for j in range(i+1, N):
            if soFar + dist[j-1][j] > horses[i][0]:
                break

            arrival = best[i] + (soFar + dist[j-1][j]) / horses[i][1]
            if best[j] == -1 or arrival < best[j]:
                best[j] = arrival
            soFar += dist[j-1][j]

    return best[-1]


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
