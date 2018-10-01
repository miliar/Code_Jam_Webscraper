import sys

def isFair(n):
    strN = str(n)
    if len(strN) == 1:
        return True

    for i in range(len(strN)/2):
        if strN[i] != strN[len(strN)-1-i]:
            return False

    return True

def isFS(n):
    sqr = n**.5
    if abs(sqr - int(sqr)) > .000001:
        return False

    if isFair(n) and isFair(int(sqr)):
        return True

def solve(A, B):
    c = 0
    for i in range(A, B+1):
        if isFS(i): c+=1

    return c


f = open('/Users/rob/Downloads/c-small-attempt0.in', 'r')

lines = f.readlines()
cases = int(lines[0])

for i in range(cases):
    tokens = lines[i+1].split()
    A = int(tokens[0])
    B = int(tokens[1])

    print('Case #'+str(i+1)+': '+str(solve(A, B)))
