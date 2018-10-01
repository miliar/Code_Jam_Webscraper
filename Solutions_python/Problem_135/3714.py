inFile = open("1.in", 'r')
outFile = open("1real.out", 'w')

def input():
    a = inFile.readline()
    print(a, end="");
    return a

def output(thing):
    print(thing)
    outFile.write(thing + "\n")

numCases = int(input())

for case in range(1, numCases+1):
    rowNum = int(input())
    for row in range(1, rowNum):
        input()
    print("real one:", end=" ")
    array = input().split()
    for row in range(rowNum, 4):
        input()

    rowNum = int(input())
    for row in range(1, rowNum):
        input()
    matches = set(array).intersection(input().split())
    for row in range(rowNum, 4):
        input()

    outLine = "Case #{0}: {1}"
    if len(matches) > 1:
        output(outLine.format(case, "Bad magician!"))
    elif len(matches) < 1:
        output(outLine.format(case, "Volunteer cheated!"))
    else:
        output(outLine.format(case, list(matches)[0]))

outFile.close()
