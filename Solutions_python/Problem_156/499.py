#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import math

def calculate(charList, D):
    intList = []
    count = 0
    for x in charList:
        if count == D:
            print "break"
            break
        intList.append(int(x))
        count += 1
        
    #print "intList = " + str(intList)
    return getMinute(intList, 0)

def divideMax(intList):
    newList = list(intList)
    maxInt = max(newList)
    newList.append(int(math.ceil(maxInt/2.0)))
    newList[newList.index(maxInt)] = int(math.floor(maxInt/2.0))
    return newList

def divideMax9(intList):
    newList = list(intList)
    maxInt = max(newList)
    newList.append(int(math.ceil(maxInt/3.0)))
    newList[newList.index(maxInt)] = int(math.floor(maxInt/1.5))
    return newList

def minus(x):
    return x-1

def AllOne(intList):
    for x in intList:
        if x != 1 :
            return False
    return True

def getMinute(pancakes, depth):
    if AllOne(pancakes):
        return 1
    #print pancakes
    maxPancake = max(pancakes)
    if maxPancake < 9:
        answer = divideMax(pancakes)
        divideAnswer = 1+ getMinute(answer, depth+1)
    else:
        answer = divideMax(pancakes)
        answer9 = divideMax9(pancakes)
        divideAnswer = 1 + min(getMinute(answer, depth+1), getMinute(answer9, depth+1))
        
            
    #print maxPancake
    #print answer, maxPancake
    
    
    if maxPancake < divideAnswer:
        #print "minus depth" + str(depth)
        #print str(maxPancake) + " < " + str(divideAnswer)
        return maxPancake
    elif maxPancake > divideAnswer :
        #print "divide depth" + str(depth)
        #print str(maxPancake) + " > " + str(divideAnswer)
        return divideAnswer
    else:
        #print "minus or divide depth" + str(depth)
        #print str(maxPancake) + " = " + str(divideAnswer)
        pass
    return divideAnswer

f = open("B-small-attempt5.in", "r")
#f = open("IHOP.in", "r")

T = int(f.readline())
for x in range(0, T):
    D = int(f.readline().strip())
    answer =  calculate(f.readline().strip().split(" "), D)
    print "Case #" + str(x+1) + ": " + str(answer)

