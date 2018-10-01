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
    d, n = readValues(int)
    horses = []
    for _ in range(n):
        horses.append(readValues(int))
    return d, horses


def solve(d, horses):
    slowest = max((d - horse[0]) / horse[1] for horse in horses)

    return d / slowest


if __name__ == '__main__':
    for _ in range(readValue(int)):
        Mouth.answer(solve(*readInput()))
