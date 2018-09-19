import os

class ParseInput:
    def __init__(self, inputFile):
        size = os.path.getsize(inputFile)
        self.openFile = open(inputFile, "r")
        self.inputFile = self.openFile.read(size)

    def parseString(self, inputSize, outputType):
        outPutArray = []
        otherArray = []
        finalArray = []
        self.tempFile = self.inputFile.split("\n")
        for i in range(1, len(self.tempFile)):
            otherArray = []
            if len(self.tempFile[i]) != "":
                self.tempFile[i] = self.tempFile[i].split(" ")
                if len(self.tempFile[i]) > 1:
                    for x in range(len(self.tempFile[i])):
                        if self.tempFile[i][x] != "":
                            otherArray.append(outputType(self.tempFile[i][x]))
                    outPutArray.append(otherArray)
                else:
                    if self.tempFile[i][0] != "":
                        outPutArray.append(outputType(self.tempFile[i][0]))
            if i % inputSize == 0:
                if len(outPutArray) > 0:
                    finalArray.append(outPutArray)
                    outPutArray = []
        return finalArray

    def simpleParse(self, inputSize):
        problem = []
        final = []
        self.tempFile = self.inputFile.split("\n")
        for i in range(1, len(self.tempFile)):
            problem.append(str(self.tempFile[i]))
            if i % inputSize == 0 and len(problem[0]) > 0:
                final.append(problem)
                problem = []
        return final

    def variableSizeParse(self, inputType):
        self.tempFile = self.inputFile.split("\n")
        problem = []
        whole = []
        final = []
        size = int(self.tempFile[1])
        start = 2
        while start + 1 <= len(self.tempFile):
            for i in range(start, size + start):
                problem = self.tempFile[i].split(" ")
                for i in range(len(problem)):
                    problem[i] = inputType(problem[i])
                whole.append(problem)
                problem = []
            final.append(whole)
            whole = []
            if self.tempFile[size + start] != "":
                tempStart = size + start + 1
                tempSize = int(self.tempFile[size + start])
                size = tempSize
                start = tempStart
            else:
                break
        return final


    def allDone(self):
        self.openFile.close()
