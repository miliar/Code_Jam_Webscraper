'''
Created on 14.04.2012

@author: Philip
'''
import math

if __name__ == '__main__':
    pass


def isNotSurprising(total, target):
    if ((3*target) - 2) <= total:
        return True
    return False

def isSurprising(total, target):
    if ((3*target) - 4) <= total:
        return True
    return False

def getResult(data):
    values = data.split()
    googlers = int(values[0]);
    surprising = int(values[1]);
    target = int(values[2])
    
    totals = values[3:]
    result = 0
    for total in totals:
        total = int(total)
        if(target == 0):
            result += 1
        if(target == 1):
            if(total > 0):
                result += 1
        if(target > 1):
            ## Need at least one judge who actually gave the target points
            if(total >= target):
                if isNotSurprising(total, target):
                    result += 1
                else:
                    if(surprising > 0):
                        if isSurprising(total, target):
                            result += 1
                            surprising -= 1
    return result    

inputFile  = open('B-large.in', 'r')
outputFile = open('B-large.out', 'w')

nrTestCases = inputFile.readline()
nrTestCases = int(nrTestCases)
currentNr = 1
while nrTestCases > 0:
    data = inputFile.readline()
    result = str(getResult(data))
    
    print "\nCase #" +str(currentNr) +": " + result
    if (currentNr > 1):
        outputFile.write("\n")
    outputFile.write('Case #'+str(currentNr)+': ' + result)
    currentNr += 1
    nrTestCases -=1

inputFile.close()        
outputFile.close()     