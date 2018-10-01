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
        self.number = words[0]
        return True
        
    def solve(self):
        """
        Return a string for the solution
        """
        numDigits = len(self.number)

        num = int(self.number)

        while True:
            #print(num)
            tidy, i = self.isTidy(num)
            if tidy:
                return num
            else:
                smallNum = int(str(num)[0:i])
                smallNum -= 1
                num = int(str(smallNum) + '9' * (numDigits - i))

    def isTidy(self, num):
        lastDigit = 0
        i = 0
        for digit in str(num):
            digit = int(digit)
            if digit < lastDigit:
                return (False, i)
            lastDigit = digit
            i += 1
        return (True, -1)

if __name__ == "__main__":
    solveTestCases()

