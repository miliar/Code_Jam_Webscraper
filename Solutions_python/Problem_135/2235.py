#!/usr/bin/python
import sys
		
data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

def getGrid(data):
    lst = []
    for x in range(4):
        temp = data.pop(0).split()
        temp = [int(y) for y in temp]
        lst.append(temp)
    return lst

for case in range(1, cases+1):
    chosenRow1 = int(data.pop(0))
    grid1 = getGrid(data)

    chosenRow2 = int(data.pop(0))
    grid2 = getGrid(data)

    choices1 = grid1[chosenRow1-1]
    choices2 = grid2[chosenRow2-1]

    common = set(choices1) & set(choices2)
    count = len(common)
    if count == 0:
        result = "Volunteer cheated!"
    elif count == 1:
        result = str(common.pop())
    else:
        result = "Bad magician!"
    
    sys.stdout.write("Case #%d: %s\n" % (case, result))