#!/usr/bin/python

""""Solve Problem B of the the Google Code Jam 2013 Qualification Round -
Lawnmower."""

import sys
import itertools


def unique(iterable):
    return list(set(iterable))

def merge(*args):
    return list(itertools.chain(*args))


class Lawn(object):
    
    MOWN = 0
    
    def __init__(self):
        self.lawn = []
        self.heights = None
        self.rows = self.cols = 0

    def read(self, ):
        rows, cols = sys.stdin.readline().strip().split(' ')
        self.rows = int(rows)
        self.cols = int(cols)
        for i in range(self.rows):
            row = [int(square) for square in sys.stdin.readline().strip().split(' ')]
            #print row
            assert len(row) == self.cols
            self.lawn.append(row)
        self.heights = sorted(unique(self.getSquares()))
        #self.prettyPrint()
    
    def prettyPrint(self):
        length = len(str(max(self.heights)))
        format = "%0" + str(length) + "i"
        for row in self.lawn:
            print ' '.join(format%(square) for square in row)
    
    def getSquares(self):
        return merge(*self.lawn)
    
    def getRow(self, rowNumber):
        return self.lawn[rowNumber]

    def getCol(self, colNumber):
        return [self.lawn[i][colNumber] for i in range(self.rows)]
    
    def _canMow(self, line):
        heights = unique(line)
        allSameHeight = len(heights) == 1 and heights[0] != self.MOWN
        allSameHeightOrMown = len(heights) == 2 and self.MOWN in heights
        return allSameHeight or allSameHeightOrMown
        
    def canMowRow(self, rowNumber):
        return self._canMow(self.getRow(rowNumber))
    
    def canMowCol(self, colNumber):
        return self._canMow(self.getCol(colNumber))
    
    def mowRow(self, rowNumber):
        assert self.canMowRow(rowNumber)
        for col in range(self.cols):
            self.lawn[rowNumber][col] = self.MOWN
        #print "Mowing row", rowNumber
        #self.prettyPrint()
    
    def mowCol(self, colNumber):
        assert self.canMowCol(colNumber)
        for i in range(self.rows):
            self.lawn[i][colNumber] = self.MOWN
        #print "Mowing col", colNumber
        #self.prettyPrint()
    
    def attemptMow(self):
        for height in sorted(self.heights):
            for col, square in enumerate(self.getRow(0)):
                if square == height or square == self.MOWN:
                    if self.canMowCol(col): self.mowCol(col)            
            for row, square in enumerate(self.getCol(0)):
                if square == height or square == self.MOWN:
                    if self.canMowRow(row): self.mowRow(row)
            if height in self.getSquares():
                return False
        return True


def main():
    numberOfLawns = int(sys.stdin.readline().strip())
    for i in range(numberOfLawns):
        print "Case #%i:"%(i+1),
        lawn = Lawn()
        lawn.read()
        if lawn.attemptMow():
            print "YES"
        else:
            print "NO"



if __name__ == '__main__':
    main()
