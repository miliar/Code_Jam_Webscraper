import sys


def getKenNumber(number, ken):
    value = 0
    for item in ken:
        if item > number:
            value = item
            break

    if value == 0:
        value = ken[0]

    return value


def war(count, naomi, ken):
    n = 0
    nIndex = len(naomi) / 2
    for i in range(count):
        if nIndex == len(naomi):
            nIndex -= 1

        nVal = naomi[nIndex]
        naomi.remove(nVal)

        kVal = getKenNumber(nVal, ken)
        ken.remove(kVal)

        if kVal < nVal:
            n += 1

    return n


def canLose(myList, hisList):
    lose = False
    for index, item in enumerate(myList):
        if myList[index] < hisList[index]:
            lose = True
    return lose


def deceit(count, naomi, ken):
    n = 0

    print naomi
    print ken

    for i in range(count):
        blockToLose = 0
        nVal = 0
        if canLose(naomi, ken):
            blockToLose = naomi[0]
            index = -1
            if i == count-1:
                index = 0
            nVal = ken[index] - .000001
        else:
            blockToLose = naomi[0]
            nVal = naomi[-1]

        naomi.remove(blockToLose)

        kVal = getKenNumber(nVal, ken)
        ken.remove(kVal)

        #print "%d %f %f" % (nVal, kVal, blockToLose)
        if kVal < nVal:
            n += 1

    return n


def questionD(count, naomi, ken):
    extraN = [num for num in naomi]
    extraK = [num for num in ken]
    warScore = war(count, naomi, ken)
    deceitScore = deceit(count, extraN, extraK)

    return deceitScore, warScore

if __name__ == '__main__':
    filename = sys.argv[1]
    text = open(filename, "r").readlines()
    testcases = int(text[0])
    text = text[1:]

    for index, line in enumerate(text):
        text[index] = line.replace('\n', '')

    outfile = open("out.txt", "a")

    for i in range(testcases):
        count = int(text[0])
        naomi = sorted([float(num) for num in text[1].split(" ")])
        ken = sorted([float(num) for num in text[2].split(" ")])

        scores = questionD(count, naomi, ken)
        result = "Case #%d: %d %d\n" % (int(i) + 1, scores[0], scores[1])
        outfile.write(result)

        print result

        text = text[3:]





