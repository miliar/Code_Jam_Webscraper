
import math



testCaseIndex = 0

class TestCase:
    def __init__(self):
        global testCaseIndex
        testCaseIndex += 1

    def parseInput(self):
        self.R, self.C, self.W = [int(x) for x in raw_input().split(" ")]

    def generateOutput(self):
        #print self.R, self.C, self.W
        self.Y = 0
        if self.R > 1:
            pass
            #self.Y += (self.R - 1) * self.C / self.W

        if self.W == 1 or self.W == self.C:
            self.Y += self.C
        else:
            self.Y += self.W + int(math.ceil((self.C - self.W) / float(self.W)))
                #while self.W < self.C:
                #self.Y += 1
                #self.C -= self.W

#self.Y += self.C + 1

        print "Case #%d: %s" % (testCaseIndex, self.Y)
        
def execTestCase():
    testcases = int(raw_input())
    for i in range(testcases):
        testCase = TestCase()
        testCase.parseInput()
        testCase.generateOutput()

execTestCase()