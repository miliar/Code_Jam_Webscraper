from io import *
from math import *

def runFile(file):
    f = open(file)
    g = open("output" + file, 'w')
    num = int(f.readline().rstrip('\n'))
    for i in range(num):
        [x,y] = (f.readline().rstrip('\n').split(' '))
        x = int(x)
        y = int(y)
        possible = True
        currentArray = []
        col = []
        row = []
        for j in range(x):
            currentArray.append((f.readline().rstrip('\n').split(' ')))
        for m in range(x):
            temp = []
            for j in currentArray[m]:
                temp.append(int(j))
            row.append(max(temp))
        for n in range(y):
            temp = []
            for m in range(x):
                temp.append(int(currentArray[m][n]))
            col.append(max(temp))
        for m in range(x):
            if(not possible):
                break
            for n in range(y):
                current = int(currentArray[m][n])
                if(current < row[m] and current < col[n]):
                    possible = False
                    break
        if(possible):
            g.write("Case #" + str(i+1) + ": YES\n")
        else:
            g.write("Case #" + str(i+1) + ": NO\n")
