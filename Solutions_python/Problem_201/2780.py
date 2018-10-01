import numpy as np
import math

class BathroomStalls:
    def readFile(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        for i in xrange(1, self.numCases + 1):
            n = map(int, raw_input().split())  # read a list of integers, 2 in this case
            self.cases.append(n)

    def printResult(self, results):
        for i in xrange(len(results)):
            n, m = results[i]
            print "Case #{}: {} {}".format(i + 1, n, m)

    def run(self):
        self.readFile()
        self.results = self.process(self.cases)
        self.printResult(self.results)

    def process(self, cases):
        results = []
        for n in cases:
            results.append(self.organiseStalls(n))

        return results

    def organiseStalls(self, n):
        numStalls, numPeople = n
        stallGaps = [numStalls]

        for _ in range(numPeople):
            largestGap = stallGaps[-1]
            stallGaps = stallGaps[:-1]
            leftFree = int(math.floor((largestGap - 1) / 2))
            rightFree = largestGap - leftFree - 1
            if largestGap == 2:
                stallGaps = stallGaps + [1]
            elif largestGap != 1:
                stallGaps = stallGaps + [rightFree, leftFree]
            stallGaps.sort()
            # print largestGap, leftFree, rightFree, stallGaps

        return max(leftFree, rightFree), min(leftFree, rightFree)

def main():
    q1 = BathroomStalls()
    q1.run()


if  __name__ =='__main__':
    main()
