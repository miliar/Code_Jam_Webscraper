# -*- coding: utf-8 -*-

# just copy a whole bunch of these just in case
import time
import sys, traceback, ast
import fileinput
import os
import re
import codecs
import math
import operator

inputFile = "B-small-attempt0.in"

outputFile = "output.txt"
outFile = open(outputFile, mode='w')

def runSolution(inFile):
    
    lines = open(inFile, mode='r').readlines()
    ln = 0 #ln = line number
    
    cases = int(lines[ln])
    ln += 1
    for i in range(0, cases):
        caseInput = []
        linesInCase = 1
        
        for j in range(0, linesInCase):
            caseInput.append(lines[ln].strip())
            ln += 1
        #ln += 1 #skip blank line in input
        
        case = formatCaseInput(caseInput)
        output = getCaseOutput(case)

        print ("Case #" + str(i+1) + ": " + output)
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    numbers = caseInput[0].split(" ")
    case = [float(numbers[0]), float(numbers[1]), float(numbers[2])]
    #print(case)
    return case

def getCaseOutput(case):
    output = doCase(case[0], case[1], case[2])
    return str(output)

def doCase(farmCost, farmBonus, goal):
    cps = 2; #cookies per second
    baseTime = goal / cps; # if you don't buy any farms at least it's this
    timeToFirstFarm = farmCost / cps;
    maxFarms = math.ceil(baseTime / timeToFirstFarm) # very bullshit but ok
    minTime = 9999999999999999999999999999999;
    for i in range(0, maxFarms+1):
        time = doCaseCheck(farmCost, farmBonus, goal, i)
        if (time < minTime):
            minTime = time
    return minTime;

def doCaseCheck(farmCost, farmBonus, goal, farmsBought):
    timeElapsed = 0;
    cps = 2;
    for i in range(0, farmsBought):
        timeToFarm = farmCost / cps;
        timeElapsed += timeToFarm
        cps += farmBonus
        
    timeToWin = goal / cps
    timeElapsed += timeToWin
    return timeElapsed

runSolution(inputFile)
