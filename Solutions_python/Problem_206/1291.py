def getAnnSpeed(start, speed, destination):
    return float(destination)/(float(destination-start)/speed)

def solve(fname):
    # READ IN AN ARRAY LINE BY LINE
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    testcasesNumber = int(content[0])
    content = content[1:]
    currentLineInFile = 0

    for t in xrange(testcasesNumber):

        D = int(content[currentLineInFile].split()[0])
        N = int(content[currentLineInFile].split()[1])
        currentLineInFile += 1

        maximumSpeed = 10000000000000.0

        for horses in xrange(N):
            K = int(content[currentLineInFile].split()[0])
            S = int(content[currentLineInFile].split()[1])
            currentLineInFile += 1
            annSpeed = getAnnSpeed(K, S, D)
            if annSpeed < maximumSpeed:
                maximumSpeed = annSpeed

        # PRINT SOLUTION
        print "Case #%d: %.6f"%((t+1), maximumSpeed)

solve("sample.txt")
