
from sys import stdin

t = int(stdin.readline())

for num in range(0, t):
    row1 = int(stdin.readline())
    for row in range(1, 5):
        rowValue = stdin.readline().strip()
        if (row == row1):
            possibilities = rowValue.split(' ')
    row2 = int(stdin.readline())
    for row in range(1, 5):
        rowValue = stdin.readline().strip()
        if (row == row2):
            found = ""
            for possibility2 in rowValue.split(' '):
                for possibility in possibilities:
                    if (possibility == possibility2):
                        if (found != ""):
                            found = "fail"
                        else:
                            found = possibility
            if (found == ""):
                toPrint = "Volunteer cheated!"
            elif (found == "fail"):
                toPrint = "Bad magician!"
            else:
                toPrint = found
            print("Case #%d: %s" % (num + 1, toPrint))

                
