#!/usr/local/bin/python2.4

import sys,os

class firstProgram:
    def __init__(self,inputFilename = "firstProgramInput.txt", outputFilename="firstProgramOutput.txt"):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename
        self.output = [] 
	self.oPosition = 1
        self.bPosition = 1
	self.oList = []
        self.bList = []
        self.rankedList = []

    
    def readInputFile(self):
        f = open(self.inputFilename,"r")
        numberOfCases = int(f.readline())
        for caseNumber in range(numberOfCases):
	    self.oPosition = 1
            self.bPosition = 1
            self.oList = []
            self.bList = []
            self.rankedList = []
            caseNumber = int(caseNumber) + 1
            inputLine = f.readline().split()
            for i in range(1,len(inputLine)):
                if str(inputLine[i]).lower() == 'o':
                    self.oList.append(int(inputLine[i+1]))
                    self.rankedList.append([0,int(inputLine[i+1])])
                if str(inputLine[i]).lower() == 'b':
                    self.bList.append(int(inputLine[i+1]))
                    self.rankedList.append([1,int(inputLine[i+1])])
                i += 1
            solution = self.solveProblem()
            self.output.append([caseNumber,solution])
        f.close()

    def canPush(self,robot="a",position=-1):
        if len(self.rankedList) and len(self.rankedList[0]):
            if self.rankedList[0][0] == robot and self.rankedList[0][1] == position:
                return 1
        return 0
    
    def push(self):
        tempRankedList = [] 
        robot = self.rankedList[0][0]
        tempRobotList = []
        if robot == 0:
            tempRobotList = self.oList[1:]
            self.oList = tempRobotList
        elif robot ==1:
            tempRobotList = self.bList[1:]
            self.bList = tempRobotList
        else:
            pass
        tempRankedList = self.rankedList[1:]
        self.rankedList = tempRankedList
        return

    def shouldMove(self,robot=-1):
        if robot == 0:
            if len(self.oList):
                if self.oPosition < self.oList[0]:
                    return 1
                if self.oPosition > self.oList[0]:
                    return -1
                if self.oPosition == self.oList[0]:
                    return 0
            return -1000
        elif robot == 1:
            if len(self.bList):
                if self.bPosition < self.bList[0]:
                    return 1
                if self.bPosition > self.bList[0]:
                    return -1
                if self.bPosition == self.bList[0]:
                    return 0
            return -1000
        else:
            return -1000
        

    def solveProblem(self):
        seconds = 0
        while(len(self.rankedList)):
            flag = 0
            if self.canPush(0,self.oPosition):
                flag = 1
                self.push()
            else:
                moveDir = self.shouldMove(0)
                if moveDir == 1:
                    self.oPosition +=1
                if moveDir == -1:
                    self.oPosition -= 1
            if not flag and self.canPush(1,self.bPosition):
                self.push()
            else:
                moveDir = self.shouldMove(1)
                if moveDir == 1:
                    self.bPosition += 1
                if moveDir == -1:
                    self.bPosition -= 1
            seconds += 1
        return seconds
                

    def writeOutput(self):
        f = open(self.outputFilename,"w")
        for case in self.output:
            f.write("Case #"+str(case[0])+": "+str(case[1])+"\n")
        f.close()
 
 

if __name__ == '__main__':
    try:
       inputFilename = sys.argv[1]
    except:
       inputFilename = "firstProgramInput.txt"
    try:
        outputFilename = sys.argv[2]
    except:
       outputFilename = "firstProgramOutput.txt" 


    fp = firstProgram(inputFilename,outputFilename)
    fp.readInputFile()
    #fp.solveProblem()
    fp.writeOutput()
 
