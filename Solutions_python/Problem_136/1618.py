import sys
import os
import shutil
import csv
import math as m
import re

#====================================
#  CONSTANTS
#====================================
# file structure related
INPUT_PATH = r"C:\Users\Dan\Dropbox\Documents\Google Code Jam\2014\Cookie Clicker\B-large.in"
OUTPUT_PATH = r"C:\Users\Dan\Dropbox\Documents\Google Code Jam\2014\Cookie Clicker\Out"

# verbose flag
# v = True
v = False

#====================================
#  MAIN FUNCTION
#====================================


def run(loadPath, outputPath):
    global cost, rate, target
    f = open(loadPath, "r")
    numCases = int(f.readline())

    output = ""

    for i in range(numCases):
        output += "Case #" + str(i + 1) + ": "

        cost, rate, target = [float(x) for x in f.readline().split()]
        if v:
            print("Cost: " + str(cost) + ", rate: " +
                  str(rate) + ", target: " + str(target))

        minimum = solveNonRecursive(2.0)
        output += str(minimum)

        output += "\n"

    fOut = open(outputPath, 'w')
    fOut.write(output)


def solveNonRecursive(currentRate):
    currentTime = float(target) / float(currentRate)
    possibleTime = float(cost) / float(currentRate) + float(target) / (currentRate + rate)
    total = float(0)

    if (currentTime < possibleTime):
        return currentTime

    while (currentTime > possibleTime):
        currentTime = target / currentRate
        possibleTime = cost / currentRate + target / (currentRate + rate)
        if v: print("Current: " + str(currentTime) + ", possible: " + str(possibleTime))

        if (currentTime > possibleTime): 
            total += cost / currentRate
            currentRate += rate
        else: break

    total += float(target) / float(currentRate)

    return total


run(INPUT_PATH, OUTPUT_PATH)
