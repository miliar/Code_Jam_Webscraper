# -*- coding: utf-8 -*-

# just copy a whole bunch of these just in case
import time
import sys, traceback, ast
import fileinput
import os
import re
import httplib
import codecs
import HTMLParser
import math
import operator

inputFile = "A-large.in"

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
        
        print "Case #" + str(i+1) + ": " + output
        outFile.write("Case #" + str(i+1) + ": " + output + '\n')
        
    outFile.close()
        

def formatCaseInput(caseInput):
    line = caseInput[0]
    splitln = line.split(" ")
    people = int(splitln[0])
    shyString = splitln[1]

    peopleArray = []
    for i in range(0, people+1):
        peopleArray.append(int(shyString[i]));

    case = []
    case.append(peopleArray)
    #print case
    return case

def getCaseOutput(case):
    val = doCase(case[0])
    return str(val)

def doCase(people):
    totalPeople = 0
    addedPeople = 0

    for i in range(0,len(people)):
        if people[i] > 0:
            while totalPeople < i:
                totalPeople += 1;
                addedPeople += 1;
            totalPeople += people[i];

    return addedPeople;
    
runSolution(inputFile)
