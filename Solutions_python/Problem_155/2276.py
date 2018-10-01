#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CodeJam:
    """A simple example class"""
    count = 0
    caseNum = 0
    filename = ""
    cases = []

    def __init__(self, caseNum, filename):
        self.caseNum = caseNum
        self.filename = filename
    
    def readInput(self):
        with open(self.filename) as f:
            lines = f.readlines()
            print("lines:{}".format(len(lines)))
            count = int(lines[0].strip())
            index = 1
            for i in range(1,len(lines),self.caseNum):
                codeCase = CodeCase(index, lines[i:i+self.caseNum])
                index = index + 1
                self.cases.append(codeCase)

    def writeOutput(self):
        with open(self.filename+".out","w+") as f:
            for case in self.cases:
                case.calculate()
                print("case:{}--{}".format(case.index, case.getOutput()))
                f.write("{}\n".format(case.getOutput()))

class CodeCase:
    """Case"""
    index = 0
    infos = []
    result = 0
    def __init__(self, index, infos):
        self.index = index
        self.infos = infos

    def printInput(self):
        print(self.infos)
        for info in self.infos:
            print(info)

    def calculate(self):
        print("calculating")
        self.result = "test"

    def getOutput(self):
        return "Case #{0}: {1}".format(self.index, self.result)

if __name__ == '__main__':
    print("codejam test")
    codejam = CodeJam(1, "/opt/work/codejam/resources/botTrust.in")
    codejam.readInput()
    codejam.writeOutput()
