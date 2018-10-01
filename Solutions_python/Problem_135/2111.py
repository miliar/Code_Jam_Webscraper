#!/usr/bin/python

import math

def rowchecker(rightRow):
        row = []
        for each in rightRow:
                row.append(int(each.strip()))
        return row;

try:
        with open("A-small-attempt0.in") as inFile, open("output.txt", "w") as outFile:
                cases = int(inFile.readline().strip())
                for c in range(cases):
                        outFile.write("Case #" + str(c+1) + ": ")
                        guess1 = int(inFile.readline().strip())
                        row1 = 0
                        firstRow = []
                        for e in range(4):
                                if guess1==row1+1:
                                        firstRow = rowchecker(inFile.readline().split(" "))
                                else:
                                        wrongRow = inFile.readline()
                                row1 = row1+1
                        guess2 = int(inFile.readline().strip())
                        secondRow = []
                        row2 = 0
                        for f in range(4):
                                if guess2==row2+1:
                                        secondRow = rowchecker(inFile.readline().split(" "))
                                else:
                                        wrongRow = inFile.readline()
                                row2 = row2 + 1
                        rightCard = 0
                        cardCounter = 0
                        for each in firstRow:
                                if each in secondRow:
                                        cardCounter = cardCounter + 1
                                        rightCard = each
                        if cardCounter == 1:
                                outFile.write(str(rightCard) + "\n")
                        elif cardCounter > 1:
                                outFile.write("Bad magician!\n")
                        elif cardCounter == 0:
                                outFile.write("Volunteer cheated!\n")
except IOError as err:
        print(str(err))
