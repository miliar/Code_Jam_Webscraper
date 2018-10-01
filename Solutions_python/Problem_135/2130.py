
import string, os, time, sys

    
def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n")
    row = int(caseline)

    firstRow = set()
    for i in range(1,5):
        caseline = f.readline().rstrip("\r\n")
        if i != row:
            continue

        cards = caseline.split(' ')
        for card in cards:
            firstRow.add(int(card))

    caseline = f.readline().rstrip("\r\n")
    row = int(caseline)

    secondRow = set()
    for i in range(1,5):
        caseline = f.readline().rstrip("\r\n")
        if i != row:
            continue

        cards = caseline.split(' ')
        for card in cards:
            secondRow.add(int(card))
    
    intersection = firstRow & secondRow

    if len(intersection) == 1:
        result = str(intersection.pop())
    elif len(intersection) == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad magician!"

    header = "Case #%(count)d: %(r)s" % {"count":caseIndex, "r":result}
    print header


inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)

