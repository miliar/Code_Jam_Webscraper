def readlines(fileName):
    fh = open(fileName, "rb")
    return [line for line in fh]

def ezprint(results, outputFile):
    with open(outputFile, "wb") as fh:
        for i, result in enumerate(results):
            print >> fh, "Case #" + str(i+1) + ": " + result

def getnums(line):
    return [int(num) for num in line.split()]

def ezsort(sortable):
    return sorted(sortable, key=lambda x: x)

results = []

lines = readlines('B.txt') #Name of input file
numTestCases = int(lines[0])

for i in range(0,numTestCases):
    line = lines[i+1]
    nums = line.split()
    C = float(nums[0])
    F = float(nums[1])
    X = float(nums[2])
    r = 2
    t = 0
    while X/(F+r) < (X-C)/r:
        t += C/r
        r += F
    results.append(str(t+X/r))

ezprint(results, 'output.txt')