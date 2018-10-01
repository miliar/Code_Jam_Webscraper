from math import *

def main():
    file = open('B-small-attempt3.in', 'r')
    cases = int(file.readline())
    for x in range(cases):
        diners = lineToIntList(file.readline())
        # print(diners)
        panckaes = lineToIntList(file.readline())
        # print(panckaes)
        answer = solve(panckaes)
        output = "Case #" + str(x+1) + ": " + str(answer)
        print(output)


def solve(line):
    timeHalf = 0
    timeSqrt = 0
    timeWithConsumeOnly = max(line)
    copyOfLine = line[:]
    while len(line) > 0:
        faster = checkFasterToEat(line)
        consumeOnly = max(line)
        if timeHalf + consumeOnly < timeWithConsumeOnly:
            timeWithConsumeOnly = timeHalf + consumeOnly
        if faster:
            consume(line)
            # print(line)
            line = removeEmpty(line)
            # print(line)
        else:
            line = moveStack(line)
        timeHalf = timeHalf + 1
    while len(copyOfLine) > 0:
        faster = checkFasterToEat(copyOfLine)
        consumeOnly = max(copyOfLine)
        if timeSqrt + consumeOnly < timeWithConsumeOnly:
            timeWithConsumeOnly = timeSqrt + consumeOnly
        if faster:
            consume(copyOfLine)
            # print(copyOfLine)
            copyOfLine = removeEmpty(copyOfLine)
            # print(copyOfLine)
        else:
            copyOfLine = moveStackSqrt(copyOfLine)
        timeSqrt = timeSqrt + 1
    best = timeHalf if timeHalf < timeSqrt else timeSqrt
    return best if best < timeWithConsumeOnly else timeWithConsumeOnly


def moveStack(line):
    line = sorted(line, reverse=True)
    # print(line)
    move = int(ceil((line[0])/2))
    # if (line[0] - move) - move <= move:
    #     move = int(ceil((line[0])/2))
    if len(line) > 1 and move >= 2 * line[1]:
        move = int(ceil(sqrt(line[0])))
    line[0] = line[0] - move
    line.append(move)
    # print(line)
    return line


def moveStackHalf(line):
    line = sorted(line, reverse=True)
    # print(line)
    move = int(ceil((line[0])/2))
    line[0] = line[0] - move
    line.append(move)
    # print(line)
    return line


def moveStackSqrt(line):
    line = sorted(line, reverse=True)
    # print(line)
    move = int(ceil(sqrt(line[0])))
    line[0] = line[0] - move
    line.append(move)
    # print(line)
    return line


def removeEmpty(line):
    return [x for x in line if x != 0]


def consume(line):
    for x in range(len(line)):
        line[x] = line[x] - 1


def checkFasterToEat(line):
    line = sorted(line, reverse=True)
    if line[0] > len(line):
        return False
    if len(line) > 1 and line[0] > line[1] + 1:
        return False
    return True


def lineToIntList(line):
    return map(int, line.strip().split())


def lineToList(line):
    return line.strip().split()

if __name__ == '__main__':
    main()
