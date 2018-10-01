class FileInput:
    def getFileLines(self, filePath):
        f = open(filePath)
        numLines = f.readline()
        allLines = []
        for index in range(int(numLines)):
            allLines.append(f.readline().strip())
        return allLines

