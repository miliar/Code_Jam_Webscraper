import math
import sys
import random

sys.setrecursionlimit(1500)

def minGreaterThan(values, minVal):
    #returns the minimum value in the list 'values' greater than minVal
    #if such a value does not exist, return the smallest value in minVal (optimal)
    inList = min(values)
    smallestGreaterThan = -1
    for value in values:
        if value > minVal and (value < smallestGreaterThan or smallestGreaterThan == -1):
            smallestGreaterThan = value
    if smallestGreaterThan == -1:
        return values.pop(values.index(inList))
    return values.pop(values.index(smallestGreaterThan))

def willNaomiWin(values, minVal):
    #returns the minimum value in the list 'values' greater than minVal
    #if such a value does not exist, return the smallest value in minVal (optimal)
    inList = min(values)
    smallestGreaterThan = -1
    for value in values:
        if value > minVal and (value < smallestGreaterThan or smallestGreaterThan == -1):
            smallestGreaterThan = value
    if smallestGreaterThan == -1:
        return False
    return True

def minGreaterThanValue(values, minVal):
    #returns the minimum value in the list 'values' greater than minVal
    #if such a value does not exist, return the smallest value in minVal (optimal)
    inList = max(values)
    smallestGreaterThan = -1
    for value in values:
        if value > minVal and (value < smallestGreaterThan or smallestGreaterThan == -1):
            smallestGreaterThan = value
    if smallestGreaterThan == -1:
        return inList
    return smallestGreaterThan




class DeceitfulWar:
    def __init__(self, naomi, ken):
        self.naomi = []
        self.ken = []
        self.naomiPoints = 0
        self.kenPoints = 0
        for i in naomi.split():
            self.naomi.append(float(i))
        for j in ken.split():
            self.ken.append(float(j))
        self.play()
    def play(self):
        #OPTIMAL STRATEGY FOR NAOMI: she cheats to remove Ken's highest
        #Then when her highest is larger than Ken's highest, she plays it
        while (len(self.naomi) > 0):
            maxKen = max(self.ken)
            maxNao = max(self.naomi)
            minKen = min(self.ken)
            minNao = min(self.naomi)
            if minNao > minKen:
                chosenNaomi = self.naomi.pop(self.naomi.index(minNao))
                toldNaomi = maxKen + 0.00001
            elif maxNao > maxKen:
                chosenNaomi = self.naomi.pop(self.naomi.index(maxNao))
                toldNaomi = maxKen - 0.00001
            else:
                chosenNaomi = self.naomi.pop(self.naomi.index(minNao))
                toldNaomi = maxKen - 0.00001
            chosenKen = minGreaterThan(self.ken, toldNaomi)
            if (chosenNaomi > chosenKen):
                self.naomiPoints+=1
            else:
                self.kenPoints+=1
                
    def score(self):
        return self.naomiPoints

class War:
    def __init__(self, naomi, ken):
        self.naomi = []
        self.ken = []
        self.naomiPoints = 0
        self.kenPoints = 0
        for i in naomi.split():
            self.naomi.append(float(i))
        for j in ken.split():
            self.ken.append(float(j))
        self.play()
    def play(self):
        while (len(self.naomi) > 0):
            #IMPLICATION: Naomi picks at random
            chosenNaomi = self.naomi.pop(random.randint(0, len(self.naomi) - 1))
            chosenKen = minGreaterThan(self.ken, chosenNaomi)
            if chosenNaomi > chosenKen:
                self.naomiPoints+=1
            else:
                self.kenPoints+=1
    def score(self):
        return self.naomiPoints
            
class TestCase:
    def __init__(self,naomi,ken):
        self.war = War(naomi,ken)
        self.dew = DeceitfulWar(naomi,ken)
    def getScores(self):
        return str(self.dew.score()) + " " + str(self.war.score())
        

infile = open('D-large.in', 'r')
outfile = open('D-large-out.txt', 'w')

cases = int(infile.readline())
for i in range(1, cases+1):
    #print(str(i) + ": ")
    n = infile.readline()
    naomi = infile.readline()
    ken = infile.readline()
    testCase = TestCase(naomi,ken)
    #print(ans)
    outfile.write("Case #" + str(i) + ": " + testCase.getScores() + "\n")

infile.close()
outfile.close()
