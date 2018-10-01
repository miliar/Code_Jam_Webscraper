#!/usr/bin/env python

class RollerCoaster:
    def __init__(self, runsPerDay, capacity):
        self.income = 0
        self.runsPerDay = runsPerDay
        self.capacity = capacity
        self.currentRun = 0
        self.peopleRiding = 0

    def run(self, group):
        while self.currentRun<self.runsPerDay:
            peopleOn = []
            while 1:
                if len(group)>0 and (self.capacity-self.peopleRiding)>=group[0]:
                    n = group.pop(0)
                    self.income += n
                    self.peopleRiding += n
                    peopleOn.append(n)
                else:
                    break
            for i in peopleOn:
                group.append(i)
            self.currentRun += 1
            self.peopleRiding = 0

class TestCase:
    def __init__(self, rpd, cap, numOfGrps, grps):
        self.grps = grps
        self.coaster = RollerCoaster(rpd, cap)

    def run(self):
        self.coaster.run(self.grps)

    def results(self):
        return str(self.coaster.income)

if __name__=='__main__':
    import sys
    inputFile = sys.argv[1]
    data = open(inputFile).read()
    numOfCases = int(data.splitlines()[0])
    outData = []
    for i in range(numOfCases):
        line = data.splitlines()[i*2+1]
        line2 = data.splitlines()[(i+1)*2]
        R, k, N = line.split(' ')
        grps = line2.split(' ')
        groups = []
        for j in grps:
            groups.append(int(j))
        case = TestCase(int(R), int(k), int(N), groups)
        case.run()
        caseData = 'Case #' + str(i+1)  + ': ' + case.results()
        outData.append(caseData)

    outFile = open(inputFile.split('.')[0]+'.out', 'w')
    outFile.write('\n'.join(outData))
