__author__ = 'Drazen'

def secondsForFactories(n, c, f):
    result = 0.0
    for i in range(n):
        result += c/(2+f*i)
    return result


def Solve(c, f, x):
    noOfFactories = 1
    lastIteration = x/2.0
    while True:
        newIteration = secondsForFactories(noOfFactories, c, f) + x/(2+f*noOfFactories)
        if newIteration >= lastIteration:
            return lastIteration
        else:
            lastIteration = newIteration
        noOfFactories+=1


if __name__ == "__main__":
    inputFile = open('H:/development/GoogleCodeJam/2014/B/B-small-attempt0.in', mode='r')
    outputFile = open('H:/development/GoogleCodeJam/2014/B/output.txt', mode='w')
    resultLine = 'Case #{0}: {1}'
    inputFile.seek(0)
    numberOfTests = int(inputFile.readline())
    for i in range(numberOfTests):
        c, f, x = map(float, inputFile.readline().split())
        result = Solve(c, f, x)
        outputFile.write(str.format(resultLine, i + 1, "%.7f" % result + '\n'))
    inputFile.close()
    outputFile.close()