def checkPancakes(pancakes):
    for pancake in pancakes:
        if (pancake == "-"):
            return False;
    return True;

def turnPancakes(pancakes, flipBegin, flipEnd):
    for i in xrange(flipBegin, flipEnd + 1):
        if (pancakes[i] == "+"):
            pancakes[i] = "-"
        else:
            pancakes[i] = "+"
    return pancakes


def oversizedPancakeFlipper(pancakes, flipQt):
    flipsCount = 0
    pancakesSz = len(pancakes)
    for i in xrange(pancakesSz):
        if (pancakes[i] == "-"):
            try:
                turnPancakes(pancakes, i, i + flipQt - 1)
            except:
                return "IMPOSSIBLE"
            flipsCount += 1
    if (not checkPancakes(pancakes)):
        return "IMPOSSIBLE"
    return flipsCount



fRead = open("A-large.in", "r")
fWrite = open("A-large-output.txt", "w")
t = fRead.readline()
lineCount = 0
for line in fRead.readlines():
    lineCount += 1
    pancakes, flipQt = line.split(" ")
    flipsCount = oversizedPancakeFlipper(list(pancakes), int(flipQt))
    fWrite.write('Case #{}: {}\n'.format(lineCount, flipsCount))
fWrite.close()

