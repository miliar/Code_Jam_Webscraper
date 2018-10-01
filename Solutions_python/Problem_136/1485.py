import sys;

sys.setrecursionlimit(15000)

def readLine(content):
    pp = content.pop(0).strip().split();
    f = [float(x) for x in pp];
    return f;

class RecSolver:
    def __init__(self, farmC, farmX, target):
        self.farmC = farmC
        self.farmX = farmX
        self.target = target
        self.farmNo = 0;

    def timeToWin(self, currTime, flowX, bestCase):
        self.farmNo += 1;
        waitTime = self.target / flowX;
        timeToFarm = self.farmC / flowX;

        diff = bestCase - currTime;

        if (waitTime <= timeToFarm):
            if (waitTime >= diff):
                print "Wait for:", bestCase
                return bestCase;

            return currTime + waitTime;
        else:
            if (timeToFarm >= diff):
                print "Wait for:", bestCase
                return bestCase;

            newBest = currTime + waitTime;
            if (newBest < bestCase):
                bestCase = newBest;

            print "Buy farm %d at: %f" % (self.farmNo, currTime + timeToFarm)
            nextTime = self.timeToWin(currTime + timeToFarm, flowX + self.farmX, bestCase);
            return nextTime;
        #end if
    #end timeToWin
#end Solver

class IterSolver:
    def __init__(self, farmC, farmX, target):
        self.farmC = farmC
        self.farmX = farmX
        self.target = target
        #self.farmNo = 0;

    def timeToWin(self, currTime, flowX, bestCase):
        while (currTime < bestCase):
            #self.farmNo += 1;
            waitTime = self.target / flowX;
            timeToFarm = self.farmC / flowX;

            diff = bestCase - currTime;

            if (waitTime <= timeToFarm):
                if (waitTime >= diff):
                    print "Wait for:", bestCase
                    nextTime = bestCase;

                return currTime + waitTime;
            else:
                if (timeToFarm >= diff):
                    print "Wait for:", bestCase
                    nextTime = bestCase;

                newBest = currTime + waitTime;
                if (newBest < bestCase):
                    bestCase = newBest;

                #print "Buy farm %d at: %f" % (self.farmNo, currTime + timeToFarm)
                #nextTime = self.timeToWin(currTime + timeToFarm, flowX + self.farmX, bestCase);
                currTime += timeToFarm;
                flowX += self.farmX

        if (currTime > bestCase):
            return bestCase

        return currTime;
            #end if
    #end timeToWin
#end Solver

def findResult(c, x, f):
    print "fr: ", c, x, f
    solver = IterSolver(c, x, f);
    return solver.timeToWin(0, 2.0, f/2.0)

def findRecResult(c, x, f):
    print "fr: ", c, x, f
    solver = RecSolver(c, x, f);
    return solver.timeToWin(0, 2.0, f/2.0)

fname = "B-large.in"
with open(fname) as f:
    content = f.readlines();

    T = int(content.pop(0))
    #print T

    with open("cook.out.txt", "w+") as fout:
        for i in range(T):
            C, F, X = readLine(content)
            res = "Case #%d: %s" % (i+1, findResult(C, F, X))
            print res

            fout.write(res)
            fout.write("\n")

