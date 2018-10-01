#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def getDigits(num):
    return int(math.log10(float(num))) + 1


def reverse(num):
  return int(str(num)[::-1])


def solve(cipher):
    num = int(cipher)
    flag = False
    if num < 20:
        return num
    if num % 10 == 0:
        flag = True
        num = num - 1
    targetDigits = getDigits(num)
    current = 12
    count = 12
    vs = [1, 10, 29, 138, 337, 1436, 3435]
    # while getDigits(current) < targetDigits:
    #     nextTarget = pow(10, getDigits(current))
    #     lastDigit = current % 10
    #     #  increament to 9 for the last digit
    #     if lastDigit < 9:
    #         newCurrent = current / 10 * 10 + 9
    #         count = count + newCurrent - current
    #     # reverse
    #     newCurrent = reverse(newCurrent)
    #     count = count + 1
    #     # add till next Target
    #     count = count + nextTarget - newCurrent
    #     current = nextTarget
    if getDigits(current) < targetDigits:
        current = pow(10, targetDigits - 1)
        count = vs[targetDigits - 1]

    if current < num:
        firstHalf = targetDigits / 2
        secondHalf = targetDigits - firstHalf

        count = count + num % pow(10, secondHalf) - (current % 10)
        rev = reverse(num / pow(10, secondHalf))
        if rev != 1:
            count = count + rev


    if flag:
        count = count + 1
    return count


if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
