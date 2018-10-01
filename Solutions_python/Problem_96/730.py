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
    p = calc(*[int(item) for item in line.split(' ')])
    outputFile.write('Case #{0}: {1}\n'.format(testNum, p))


def calc(n, s, p, *scores):
    numScoresGteP = 0
    oneLessP = p - 1
    for total in scores:
        avg = int((total / 3.0) + 0.5)
        remainder = total - 2 * avg
        triplet = [avg, avg, remainder]
        if(avg != 0 and avg >= remainder and avg == oneLessP and s > 0):
            triplet[0] += 1
            triplet[1] -= 1
            s -= 1
        if(max(triplet) >= p):
            numScoresGteP += 1

    return numScoresGteP


if __name__ == '__main__':
    main()
