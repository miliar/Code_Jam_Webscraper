# -*- encoding: utf-8 -*-
"""
Diminishing Cookie Recursion
"""
from __future__ import division
import sys
sys.setrecursionlimit(10000)


COOKIE_RATE = 2


def maxCookieConsumption(farmCost, farmRate, desiredCookies, seconds=0, currentRate=COOKIE_RATE):
    """Cookie Monster of a Headache

    :param desiredCookies: cookies desired
    :param farmCost: cost per farm
    :param farmRate: yield per farm
    :param seconds: keeping track through recursion
    :param currentRate: keeping track through recursion
    :return:
    """
    noNewFarmSeconds = desiredCookies / currentRate + seconds
    withNewFarmSeconds = desiredCookies / (currentRate + farmRate) + (farmCost / currentRate) + seconds
    if withNewFarmSeconds > noNewFarmSeconds:  # too expensive
        return noNewFarmSeconds

    seconds += farmCost / currentRate
    currentRate += farmRate
    return maxCookieConsumption(farmCost, farmRate, desiredCookies, seconds, currentRate)


def stripSplitLine(line):
    return map(float, line.strip().split())


inputFile = open('input.txt')
resultsFile = open('results.txt', 'w')

numCases = int(inputFile.readline().strip())

for i in range(numCases):
    inputs = stripSplitLine(inputFile.readline())
    resultsFile.write('Case #{0}: {1}\n'.format(i + 1, maxCookieConsumption(*inputs)))
