#   CodeJam 2013
#   Nick: mnganesh
#   Description: Problem B. Lawnmower

__author__ = 'Ganesh'

import fileIO

ifileName = "i.txt"
ofileName = "2AOutput.txt"

def getLawnArray(ifDump):
    nCases = int(ifDump[0])
    lawns = []
    line = 1
    for case in xrange(nCases):
        nrow,ncol = map(int,ifDump[line].split())
        lawn = []
        line+=1
        for i in xrange(nrow):
            row = map(int, ifDump[line].split())
            lawn.append(row)
            line+=1
        lawns.append(lawn)
    return lawns


def main():
    ifDump = fileIO.readFile(ifileName)
    lawnArray = getLawnArray(ifDump)
    solArr = []
    for l in lawnArray:
        lawn = Lawn(l)
        if lawn.check():
            solArr.append("YES")
        else:
            solArr.append("NO")
    fileIO.outFile(ofileName, solArr)


class Lawn:
    def __init__(self,lawn):
        self.__lawn = lawn
        self.__freshLawn = []
        self.nrow = len(lawn)
        self.ncol = len(lawn[0])
        for row in xrange(self.nrow):
            row = []
            for col in xrange(self.ncol):
                row.append(100)
            self.__freshLawn.append(row)

    def check(self):
        self.__cutRows()
        self.__cutCols()
        return self.__lawn == self.__freshLawn


    def __cutRows(self):
        rowi=0
        for row in self.__lawn:
            maxHeight = max(row)
            for col in xrange(len(row)):
                if self.__freshLawn[rowi][col] > maxHeight:
                    self.__freshLawn[rowi][col] = maxHeight
            rowi += 1

    def __cutCols(self):
        for col in xrange(self.ncol):
            maxHeight = 0
            for row in xrange(self.nrow):
                maxHeight = max(self.__lawn[row][col], maxHeight)
            for row in xrange(self.nrow):
                if self.__freshLawn[row][col] > maxHeight:
                    self.__freshLawn[row][col] = maxHeight

if __name__== '__main__':
    main()