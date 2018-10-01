


import sys

inputFilename = sys.argv[1]


with open(inputFilename,'r') as f:
    lines = f.readlines()
    noTestCases = int(lines[0])
    testCase = 1
    currentLine = 1
    while testCase <= noTestCases:
        D,N = lines[currentLine].rstrip().split()
        D = int(D)
        N = int(N)
        horses = [list(map(int,lines[currentLine+i+1].rstrip().split())) for i in range(N)]

        slowest = -1
        #Time for slowest
        for horse in horses:
            time = (D - horse[0])/horse[1]
            if time > slowest:
                slowest = time
        print("Case #%d: %.7f" % (testCase, D/slowest))

        currentLine += (N+1)
        testCase += 1



