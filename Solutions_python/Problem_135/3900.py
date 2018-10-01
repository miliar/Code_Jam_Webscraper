import sys

def readint():
    return map(int, sys.stdin.readline().split(' '))
    
t = readint()[0]

badString = "Bad magician!"
cheatStr = "Volunteer cheated!"
resultString = "Case #{0}: {1}"

for i in range(1, t+1):
    a = readint()[0]
    first = []
    for skip in range(1, 5):
        d = readint()
        if (skip == a):
            first = d
    
    b = readint()[0]
    second = []
    for skip in range(1, 5):
        d = readint()
        if (skip == b):
            second = d

    first = set(first)
    second = set(second)
    result = first.intersection(second)
    
    res = len(result)
    if (res == 0):
        print str.format(resultString, i, cheatStr)
    elif (res == 1):
        print str.format(resultString, i, result.pop())
    else:
        print str.format(resultString, i, badString)
    
        