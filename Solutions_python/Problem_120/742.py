#! /usr/bin/python
import math

def calcPNeeded(innerRad):
   outerRad = innerRad + 1
   return (outerRad * outerRad) - (innerRad * innerRad)

fp = open("input.txt","r")

outputList = []
for caseNo in range(int(fp.readline())):
   inputString = fp.readline()
   inputList = inputString.split()
   origRad = int(inputList[0])
   mLPaint = int(inputList[1])
   i = 0
   innerRad = origRad
   while mLPaint >= 0:
      #print mLPaint
      mLPaint -= calcPNeeded(innerRad)
      innerRad += 2
      i += 1
   outputList.append(str(i - 1))
   
fp.close()
outputString = ""
for x in range(len(outputList)):
   outputString += "Case #" + str(x + 1) + ": " + outputList[x] + "\n"

fp = open("output.txt","w")
fp.write(outputString)
fp.close()
