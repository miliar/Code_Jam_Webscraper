#!/usr/bin/python3
from __future__ import print_function
import sys


def isTidy(number):
    nstring = str(number)
    previous = '0'
    for char in nstring:
        if char < previous:
            return False
        previous = char
    return True


def makeTidyOneDigit(number):
    nstring = str(number)
    previous = '0'
    for i, char in enumerate(nstring):
        if char < previous:
            if char == '0' and previous == '1' and i == 1:
                return ('9' * (len(nstring) - i))
            else:
                return nstring[:i-1] + str(int(previous) - 1) + ('9' * (len(nstring) - i))
        previous = char
    return number


def makeTidyNumber(number):
    curNum = number
    while not isTidy(curNum):
        curNum = makeTidyOneDigit(curNum)
    return curNum


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = int(lines[0])
for i in range(n):
    num = int(lines[i+1])
    numIsTidy = isTidy(num)
    if numIsTidy:
        tidyNum = num
    else:
        tidyNum = makeTidyNumber(num)
    print('Case #' + str(i+1) + ': ' + str(tidyNum))
