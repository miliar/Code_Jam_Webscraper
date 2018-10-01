import sys
sys.setrecursionlimit(10000) 

f = open('B-small-attempt0.in', 'r')

def nextline():
    return f.readline().replace('\n', '')

testcount = int(nextline())

def timeWithOneMoreFarm(cost, goal, farmProductivity, currProductivity, currWaitTime, bestTimeUntilGoal):
    timeUntilFarm = cost / currProductivity;
    newProductivity = currProductivity + farmProductivity
    newWaitTime = currWaitTime + timeUntilFarm
    timeUntilGoal = newWaitTime + goal / newProductivity;
    if (timeUntilGoal >= bestTimeUntilGoal):
        return bestTimeUntilGoal
    else:
        return timeWithOneMoreFarm(cost, goal, farmProductivity, newProductivity, newWaitTime, timeUntilGoal)

for i in range(testcount):
    caseDesc = nextline().split(' ')
    costPerFarm = float(caseDesc[0])
    productivityFarm = float(caseDesc[1])
    goal = float(caseDesc[2])
    timeToWait = goal / 2.0
    bestTime = timeWithOneMoreFarm(costPerFarm, goal, productivityFarm, 2.0, 0, timeToWait)
    
    print("Case #%d: %f" %((i+1), bestTime))