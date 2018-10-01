#!/bin/python  

import string

def findLastTidyNum(N):
    i = N
    while(i > 0):
        if (isTidy(i)):
            return i
        else:
            i = int(i)-1

def isTidy(i):
    if (numOfDigits(i) == 1):
        return True
    else:
        res = True
        count = 0
        while (res == True and count < numOfDigits(i) - 1):
            if ( str(i)[count] <= str(i)[count +1]):
                count = count + 1
            else:
                res = False
        return res

def numOfDigits(i):
    res = 0
    while ( int(i) > 9 ):
        res = res + 1
        i = int(i)/10
    return res + 1

T = raw_input()

for i in range(0, int(T)):
    N = raw_input()
    print ("Case #" + str(i + 1)  + ": " + str(findLastTidyNum(N)))