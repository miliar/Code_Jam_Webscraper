#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      qmarchal
#
# Created:     11/04/2013
# Copyright:   (c) qmarchal 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import math
f = open("1.in")
T = int(f.readline())
palList = []

def writeOutput(output):
    w = open("ouput.txt","w")
    w.write(output)
    w.close()
def nextInt():
    return int(f.readline())
def nextList():
    return f.readline().split()
def nextIntList():
    strings = f.readline().split()
    ints = []
    for string in strings:
        ints.append(int(string))
    return ints
def nextStr():
    return f.readline()
def main():
    output = "";
    for x in range(0, 10000000):
        if isPalin(x):
            xx = x*x
            if (xx>100000000000000):
                break
            if isPalin(xx):
##                if (A<=xx<=B):
                palList.append(xx)
    for t in range(1,T+1,1):
        output +="Case #%d: "%t + case() + "\n"
    writeOutput(output)
def isPalin(x):
    y = str(int(x))[::-1]
    if (str(int(x))==y):
        return True
    return False
def case():
    output = ""
    A,B = nextIntList()
    count = 0
    for i in range(0,len(palList),1):
        if A<=palList[i]<=B:
            count+=1
        elif palList[i]>B:
            break
##    for x in range(int(math.sqrt(A)), int(math.sqrt(B)+1),1):
##        if isPalin(x):
##            xx = x*x
##            if (xx>B):
##                break
##            if isPalin(xx):
##                if (A<=xx<=B):
##                    count+=1
##                    list.append(xx)
    output += str(count)
    return output
if __name__ == '__main__':
    main()
