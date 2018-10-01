
def readInput(filename):
    inputFile = open(filename)
    lines = int(inputFile.readline())
    cases = []
    for _ in range(lines):
        line = inputFile.readline().strip()
        values = line.split(' ')
        cases.append((int(values[0]), int(values[1])))
    return cases

def solveProblem(cases):
    result = []
    for case in cases:
        result.append(solveCase(case[0], case[1]))
    return result

def solveCase(minValue, maxValue):
    result = 0
    for n in range(minValue, maxValue):
        result += findRecycled(n, maxValue)
    
    return result

def findRecycled(n, maxValue):
    found = set()
    s = str(n)
    length = len(s)
    for _ in range(len(s) - 1):
        s = s[-1] + s[:-1]
        m = int(s)
        if (n >= m): continue
        if m > maxValue: continue
        if not len(str(m)) == length: continue
        found.add(m)
        
    return len(found)

def outputResults(results):
    outputFile = open('C-large.out', 'w')
    for idx in range(len(results)):
        result = 'Case #%d: %d\n' % (idx + 1, results[idx])
        outputFile.write(result)
    outputFile.close()
    
if __name__ == '__main__':
    cases = readInput('C-large.in')
    results = solveProblem(cases)
    outputResults(results)

    