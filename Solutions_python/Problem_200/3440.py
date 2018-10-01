# given n split as a list
def lastTidy(n):
    nList = list(str(n))
    for i in range(len(nList)):
        nList[i] = int(nList[i])
    oList = []
    i = 0
    while ((i < len(nList) - 1) and (nList[i] <= nList[i+1])):
        oList.append(nList[i])
        i += 1
    oList.append(nList[i])
    if (i != len(nList) -1):
        for j in range(i+1, len(nList)):
            oList.append(9)
        oList[i] -= 1
        while (i > 0):
            if oList[i -1] > oList[i]:
                oList[i - 1] = oList[i - 1] - 1
                oList[i] = 9
                i -= 1
            else:
                break
    if (oList[i] <= 0):
        oList.pop(0)
    myStr = ''
    for elem in oList:
        myStr += str(elem)
    return int(myStr)

with open('B-small-attempt0.in', 'r') as f:
    lineCount = 0
    for line in f:
        if lineCount == 0:
            lineCount += 1
            continue
        else:
            n = int(line.strip())
            print('Case #{}: {}'.format(lineCount, lastTidy(n)))
            lineCount += 1
