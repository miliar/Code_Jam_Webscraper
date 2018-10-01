'''
Created on 12-Apr-2014

@author: Pankaj
'''
import os, sys

def solveCase(farmCost, farmCookieRate, targetCookies):
    def timeForTarget(crntRate):
        return float(targetCookies) / crntRate
    
    def timeForFarm(crntRate):
        return float(farmCost) / crntRate
    
    timeTaken = 0
    crntCookieRate = 2
    
    while True:
        targetTime = timeForTarget(crntCookieRate)
        
        farmTime = timeForFarm(crntCookieRate)
        newCookieRate = crntCookieRate + farmCookieRate
        withFarmTime = farmTime + timeForTarget(newCookieRate)
        
        if targetTime < withFarmTime:
            return timeTaken + targetTime
        crntCookieRate = newCookieRate
        timeTaken += farmTime
        
inputFile = sys.argv[1]
fileHandle = file(inputFile, "r")
fileData = fileHandle.readlines()
fileHandle.close()

nTests = int(fileData[0].replace("\n", "").replace(" ", ""))

outputFile = os.path.splitext(inputFile)[0] + ".out"
if os.path.exists(outputFile):
    os.remove(outputFile)
fileHandle = file(outputFile, "w")

for i, eachCase in enumerate(fileData[1:]):
    inputData = eachCase[:-1].split(" ")
    timeTaken = solveCase(float(inputData[0]), float(inputData[1]), float(inputData[2]))
    fileHandle.write("Case #%d: %s\n" % (i+1, timeTaken))
fileHandle.close()
