def findFirstLarger(value, L):
    for i in range(len(L)-1,0-1,-1):
        if L[i] > value:
            return i
    return -1

file = open("in.txt")
file2 = open("out.txt",'w')

lineNumber = 0
for line in file:
    if lineNumber == 0 or lineNumber % 3 == 1:
        lineNumber += 1
        continue
    elif lineNumber % 3 == 2:
        naomiBlocks = line.strip().split()
        lineNumber += 1
        continue
    # lineNumber % 3 == 0:
    kenBlocks = line.strip().split()
    for i in range(len(naomiBlocks)):
        naomiBlocks[i] = float(naomiBlocks[i])
        kenBlocks[i] = float(kenBlocks[i])
    naomiBlocks.sort(reverse=True)
    naomiBlocks2 = naomiBlocks[:]
    kenBlocks.sort(reverse=True)
    kenBlocks2 = kenBlocks[:]
    
    cheatingPoints = 0
    while len(naomiBlocks) > 0:
        val = kenBlocks.pop()
        index = findFirstLarger(val, naomiBlocks)
        if index == -1:
            break
        else:
            naomiBlocks.pop(index)
            cheatingPoints += 1

    legitPoints = 0
    while len(naomiBlocks2) > 0:
        val = naomiBlocks2.pop()
        index = findFirstLarger(val, kenBlocks2)
        if index == -1:
            legitPoints += 1
            kenBlocks2.pop()
        else:
            kenBlocks2.pop(index)

    print(lineNumber)
    file2.write("Case #{}: {} {}\n".format(lineNumber//3, cheatingPoints, legitPoints))

    lineNumber += 1

file2.close()



