from __future__ import division, print_function
import string
import re

def cj3(fInP="in.txt", fOutP="out.txt"):
    fIn = open(fInP, 'r')
    fOut = open(fOutP, 'w')
    N = int(fIn.readline())
    find = "welcome to code jam"
    for n in range(0, N):
        txt = fIn.readline()
        pointer1 = [(-1, 1)]
        for nextChar in find:
            pointer2 = []
            for m in re.finditer(nextChar, txt):
                p2Pos = m.start()
                p2Count = 0
                for p1 in pointer1:
                    p1Pos, p1Count = p1
                    if (p1Pos < p2Pos):
                        p2Count += p1Count
                p2 = (p2Pos, p2Count)
                pointer2.append(p2)
            pointer1 = pointer2
        solutions = 0
        for p1 in pointer1:
            solutions += p1[1]
        solutionsStr = '0000' + str(solutions)
        solutionsDDDD = solutionsStr[len(solutionsStr)-4:]
        fOut.write('Case #' + str(n+1) + ': ' + str(solutionsDDDD) + '\n')

