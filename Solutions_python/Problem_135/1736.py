def findFirstLarger(value, L):
    for i in range(len(L)-1,0-1,-1):
        if L[i] > value:
            return i
    return -1

file = open("in.txt")
file2 = open("out.txt",'w')

lineNumber = 0
for line in file:
    if lineNumber == 0:
        pass
    elif lineNumber % 10 in (1,6):
        rowNum = int(line.strip())
        rows = []
    elif lineNumber % 10 in (2,3,4,7,8,9):
        rows.append(line.strip().split())
    elif lineNumber % 10 == 5:
        rows.append(line.strip().split())
        options = rows[rowNum-1]
    elif lineNumber % 10 == 0:
        rows.append(line.strip().split())
        options2 = rows[rowNum-1]
        finalAnswer = []
        for n in options:
            if n in options2:
                finalAnswer.append(n)
        if len(finalAnswer) < 1:
            s = "Volunteer cheated!"
        elif len(finalAnswer) > 1:
            s = "Bad magician!"
        else:
            s = finalAnswer[0]
        file2.write("Case #{}: {}\n".format(lineNumber//10,s))
    lineNumber += 1

file2.close()



