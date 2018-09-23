import math

def solveTestCases():
    import fileinput, sys
    solver = None
    caseNum = 0
    numCases = 0
    for line in fileinput.input():
        line = line.strip('\n')
        if line == '':
            continue
        if fileinput.isfirstline():
            numCases = int(line)
        else:
            if solver is None:
                solver = Solver()
                caseNum += 1
                lineNum = 0
            words = line.split(' ')
            if solver.readLine(lineNum, words): # if this is the last line
                print("Case #" + str(caseNum) + ":", solver.solve())
                solver = None
            lineNum += 1
    if caseNum == 0:
        print("ERROR: No cases!", file=sys.stderr)
    elif caseNum != numCases:
        print("ERROR:", numCases, "expected,", caseNum, "solved.",
              file=sys.stderr)


class Solver:

    def __init__(self):
        pass

    def readLine(self, lineNum, words):
        """
        Interpret a line from input. lineNum is an int starting at 0. words is a
        list of strings.
        Return True if this is the last line.
        """
        self.numStalls = int(words[0])
        self.numPeople = int(words[1])
        self.stallDists = [self.numStalls+1]
        return True
        
    def solve(self):
        """
        Return a string for the solution
        """
        person = 0
        while person < self.numPeople:
            #print(self.stallDists)
            largestDist = 0
            distI = [ ]
            j = 0
            for dist in self.stallDists:
                if dist > largestDist:
                    largestDist = dist
                    distI = [j]
                elif dist == largestDist:
                    distI.append(j)
                j += 1
            left = math.floor(float(largestDist) / 2)
            right = math.ceil(float(largestDist) / 2)

            #print(distI)
            for i in distI:
                if person >= self.numPeople:
                    break
                self.stallDists[i] = left
                self.stallDists.append(right)
                person += 1
        #print(self.stallDists)
        return str(right-1) + " " + str(left-1)

if __name__ == "__main__":
    solveTestCases()

