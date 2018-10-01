import subprocess
import os

currentWorkingDirectory = os.getcwd()



testInputFile = open(currentWorkingDirectory + '/testinput')
testOutputFile = open(currentWorkingDirectory + '/A-small-attempt0.out', 'w')
numberOfTestCases = testInputFile.readlines()[2]
caseNumber = 0
panCakes = ""
flipSize = 0

def toggleInput(str):
    if(str == '+'):
        return '-'
    else:
        return '+'


def computeFlips(cakeStateList, flipSize):
    flipCounter = 0
    cakeLoopCounter = 0
    newCakeStateList = []
    
    
    while(True):
        i = len(cakeStateList)
        for i in range(len(cakeStateList) - flipSize + 1):
            if(cakeStateList[i] == '+'):
                continue
            else:
                flipCounter = flipCounter + 1
                for sizeCounter in range(flipSize):
                    cakeStateList[i+ sizeCounter] = toggleInput(cakeStateList[i + sizeCounter])
                
        break
    
    print(cakeStateList)
    print(flipCounter)
    if('-' in cakeStateList):
        return "IMPOSSIBLE"
    else:
        return flipCounter





print("number of Test Cases : ", numberOfTestCases)
inputList = []

for linenumber, line in enumerate(open(currentWorkingDirectory + '/testinput', 'r')):
       
    if(len(line.split()) == 2):
        caseNumber += 1
        testOutputFile.write("Case #" + repr(caseNumber) + ": ")
        
        [panCakes, flipSizeString] = line.split()
        cakeStateList = list(panCakes)
        flipSize = int(flipSizeString)
        testOutputFile.write(str(computeFlips(cakeStateList, flipSize)))
        testOutputFile.write("\n")

        
        