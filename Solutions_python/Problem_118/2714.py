import gmpy2
import math
import sys
sys.setrecursionlimit(5000)
def getNumDigits(x):
    i = 1
    while x/10 != 0:
        i += 1
        x /= 10
    return i
def checkPal(x):
    n = x
    y = 0
    while n > 0:
        y = y*10 + n%10
        n /= 10
    return x == y

L = {}
def generate(numDigits):
    if numDigits == 0:
        L[0] = [0]
        return [0]
    if numDigits == 1:
        L[1] = [0, 1, 2, 3]
        return [0, 1, 2, 3]
    if numDigits in L:
        return L[numDigits]
    pal = []
    for p in generate(numDigits-2):
        pal.append(p)
    for p in generate(numDigits-2):
        for i in [1, 2]:
            n = i*(10**(numDigits-1)) + p*10 + i
            if checkPal(n**2):
                pal.append(n)
    L[numDigits] = pal
    return pal
def p3(inName, outName):
    inFile = open(inName, "r")
    outFile = open(outName, "w")
    T = int(inFile.readline())
    for t in range(T):
        A, B = map(int, inFile.readline().split())
        digitsA = getNumDigits(A)
        digitsB = getNumDigits(B)
        generate(digitsB/2)
        generate(digitsB/2 + 1)
        L1 = set(L[digitsB/2])
        L1.update(L[digitsB/2+1])
        L2 = map(lambda x: x**2, L1)
        L2.sort()
        k = 0
        for n in L2:
            if n < A:
                continue
            elif n > B:
                break
            k += 1
        outFile.write("Case #" + str(t+1) + ": " + str(k))
        outFile.write("\n")
def p3_bruteforce(inName, outName):
    inFile = open(inName, "r")
    outFile = open(outName, "w")
    T = int(inFile.readline())
    for t in range(T):
        A, B = map(int, inFile.readline().split())
        sA = int(math.sqrt(A))
        sB = int(math.sqrt(B))
        k = 0
        for s in range(sA, sB + 1):
            s2 = s**2
            if s2 < A:
                continue
            if s2 > B:
                break
            if checkPal(s) and checkPal(s2):
                k += 1
        outFile.write("Case #" + str(t+1) + ": " + str(k))
        outFile.write("\n")
        
    
        
p3('C-small-attempt1.in', 'C-small-attempt1.out')
#p3_bruteforce('C-small-attempt0.in', 'C-small-attempt0.out_')