import math

def getOpNum(nList, desireMax):
    opSum = 0
    for n in nList:
        if n <= desireMax:
            break
        op = math.ceil(n / desireMax) - 1
        opSum += op
    return opSum    

def solve(caseNo, nList):
    nList.sort(reverse=True)
    ansList = [desireMax + getOpNum(nList, desireMax) for desireMax in range(1, max(nList)+1)]
    print('Case #%d: %d' % (caseNo, min(ansList)))

fin = open('B-large.in')

caseNum = int(fin.readline())
for caseNo in range(caseNum):
    D = int(fin.readline())
    nList = list(map(int, fin.readline().strip().split()))
    solve(caseNo+1, nList)

fin.close()


    
