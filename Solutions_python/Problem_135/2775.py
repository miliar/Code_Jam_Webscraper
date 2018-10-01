__author__ = 'MERT'

inp = open("A-small-attempt0.in","r")
output = open("output.txt","w")
line = inp.readline()
numberOfTest = int(line)
for case in range(1,numberOfTest+1):
    row1 = int(inp.readline())
    rows1 = []
    for satir in range(1,5):
        rows1.append([])
        line = inp.readline()
        numbers = line.split(' ')
        for number in numbers:
            rows1[satir-1].append(int(number))

    row2 = int(inp.readline())
    rows2 = []
    for satir in range(1,5):
        rows2.append([])
        line = inp.readline()
        numbers = line.split(' ')
        for number in numbers:
            rows2[satir-1].append(int(number))

    compareList1 = rows1[row1-1]
    compareList2 = rows2[row2-1]

    results = []
    for x in compareList1:
        for y in compareList2:
            if x==y:
                results.append((x))
                break
    if len(results) == 0:
        output.writelines("Case #" + str(case) + ": Volunteer cheated!\n")
    elif len(results) == 1:
        output.writelines("Case #" + str(case) + ": " + str(results[0]) + "\n")
    else:
        output.writelines("Case #" + str(case) + ": Bad magician!\n")
output.close()