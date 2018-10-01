#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

inFile = open("input.txt","r")
outFile = open("output.txt","w")

def isTidy(numstr):
    bTidy = True
    last = -1
    for i in range(len(numstr)):
        num = int(numstr[i])
        if i != 0:
            if num == 0:
                bTidy = False
            if num < last:
                bTidy = False
        if not bTidy:
            break
        last = num
    return bTidy


def solve(case, number):
    tidy = number
    while True:
        if isTidy(str(tidy)):
            break

        last = -1
        for i in range(len(str(tidy))):
            num = int(str(tidy)[i])
            if num < last:
                tidy = tidy - (int(str(tidy)[i:]) + 1)
                print tidy
                break
            last = num
    return "Case #%d: %d\n" % (case, tidy)

if __name__ == "__main__":
    isFirst = True
    totalCase = 0
    currentCase = 1

    for line in inFile.readlines():
        items = line.split()

        # first Line
        if isFirst == True:
            isFirst = False
            totalCase = int(items[0])
            continue

        # execute
        out = solve(currentCase, int(items[0]))
        outFile.write(out)
        print out.rstrip()

        # go next
        currentCase = currentCase + 1
        if currentCase > totalCase:
            break

