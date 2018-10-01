'''
Created on 2012-4-14

@author: hemnd
'''
from time import clock as now

ln = [[]]*2000000

def cal(A, B):
    a = int(A)
    b = int(B)
    lm = [False]*(10 ** len(B))
    rslt = 0
    for n in range(a, b):
        if lm[n - a]:
            continue
        if len(ln[n]) != 0:
            tmp = 1
            for m in ln[n]:
                if m <= b:
                    tmp += 1
                    lm[m - a] = True
            if tmp == 1:
                tmp = 0
            elif tmp == 2:
                tmp = 1
            elif tmp == 4:
                tmp = 6
            elif tmp == 5:
                tmp = 10
            elif tmp == 6:
                tmp = 15
            rslt += tmp
            continue
        tmp = 1
        for i in range(1, len(A)):
            m = int(str(n)[-i:] + str(n)[:len(A) - i])
            if lm[m - a]:
                continue
            if m > n:
                ln[n] = ln[n] + [m]
                if m <= b:
                    tmp += 1
            lm[m - a] = True
        if tmp == 1:
            tmp = 0
        elif tmp == 2:
            tmp = 1
        elif tmp == 4:
            tmp = 6
        elif tmp == 5:
            tmp = 10
        elif tmp == 6:
            tmp = 15
        rslt += tmp
    return rslt

start = now()
inputFile = open('C-large.in', 'r')
#inputFile = open('test.txt', 'r')
inputLines = inputFile.readlines()
inputFile.close()

T = int(inputLines[0])
outputLines = []

for i in range(1, T + 1):
    args = inputLines[i].strip().split(' ')
    outputLines.append('Case #%d: %d\n' % (i, cal(args[0], args[1])))
    print outputLines[i - 1],

outputFile = open('C-large.out', 'w')
outputFile.writelines(outputLines)
outputFile.close()
finish = now()
print finish - start
