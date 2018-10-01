import sys


def main():
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    with open(inputFile) as infile, open(outputFile,'w') as output:
        infile.readline()
        lineNum = 0
        for line in infile:
            lineNum += 1
            runTestCase(lineNum, line, output)


def runTestCase(testNum, line, outputFile):
    a, b = [int(item) for item in line.split(' ')]
    numPairs = calcNumPairs(a, b)

    outputFile.write('Case #{0}: {1}\n'.format(testNum, numPairs))


def calcNumPairs(a, b):
    if(numDigit(a) < 2 or numDigit(b) < 2):
        return 0

    recycled_pairs = set()

    for n in range(a, b + 1):
        pairGenerator = createPairGenerator(n)
        nNumDigits = numDigit(n)
        for m in pairGenerator:
            if isValidPair(n, m, a, b):
                recycled_pairs.add(frozenset([n, m]))

    return len(recycled_pairs)


def isValidPair(n, m, a, b):
    if m < a or m > b:
        return False
    if numDigit(n) != numDigit(m):
        return False
    if n == m:
        return False
    return True


def numDigit(num):
    return len(str(num))


def createPairGenerator(n):
    pair = str(n)
    for i in range(numDigit(n) - 1):
        pair = pair[-1] + pair[:-1]
        yield int(pair)

if __name__ == '__main__':
    main()
