'''
Created on Apr 12, 2014

@author: Miguel Provencio
'''

from sys import stdin

class CaseCount:
    def __init__(self):
        pass
    def parseCaseCount(self):
        line = stdin.readline().strip()
        self.count = int(line)
        
class CookieClicker:
    def __init__(self):
        pass
    def getInput(self):
        line = stdin.readline().strip()
        vars = line.split(" ")
        self.farmCost = float(vars[0])
        self.farmRate = float(vars[1])
        self.winCost = float(vars[2])
        
    def __str__(self):
        s = "Farm cost: %f\n" % self.farmCost
        s = s + "Farm rate: %f\n" % self.farmRate
        s = s + "Win cost: %f\n" % self.winCost
        return s            
    
    def simulate(self):
        farms = 0
        rate = 2.0
        t = 0.0
        self.tWin = {}
        while True:
            self.tWin[farms] = t+(self.winCost/rate)
            if farms > 0 and self.tWin[farms] > self.tWin[farms-1]:
                break
            tFarm = self.farmCost/rate
            t = t + tFarm
            farms += 1
            rate = rate + self.farmRate
        
        self.minTime = 0.0
        for farms in self.tWin:
            if self.minTime == 0.0 or self.tWin[farms] < self.minTime:
                self.minTime = self.tWin[farms]
                
    def output(self,case):
        print "Case #%d: %.7f" % (case,self.minTime)

if __name__ == "__main__":
    caseCount = CaseCount()
    caseCount.parseCaseCount()
    for i in range(caseCount.count):
        cookieClicker = CookieClicker()
        cookieClicker.getInput()
        cookieClicker.simulate()
        cookieClicker.output(i+1)
