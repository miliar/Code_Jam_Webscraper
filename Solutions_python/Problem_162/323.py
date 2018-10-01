#!/usr/bin/python
from __future__ import print_function
from sys import stdin
log = open("C:\\Users\\tx_2\Documents\\Coding\\Google Code Jam 2015\\1B\\A-small-output.txt", "w")

def readiline():
    return map( int, stdin.readline().strip().split() )

def readsline():
    return map( str, stdin.readline().strip().split() )

def reverseNum(x):
    xstr = str(x)
    xstr = xstr[::-1]
    return int(xstr)

def numFlips(m,n):
    #returns number of things you need to say from 1 to n
    maxdif = 0
    maxnum = 0
    for j in range(m,n+1):
        reversedj = reverseNum(j)
        if (reversedj > j + 1) and (reversedj <= n):
            if (reversedj - j) > maxdif:
                maxdif = reversedj - j
                maxnum = j

    if maxdif == 0:
        #print(m-n+1)
        return n-m+1
    else:
        return numFlips(m,maxnum) + numFlips(reverseNum(maxnum), n)
T, = readiline()




for i in xrange(1,T+1):
    N = readiline()
    curr = N[0]
    # count = 1
    # while curr > 1:
    #     count += 1
    #     reverseCurr = reverseNum(curr)
    #     # print(curr)
    #     # print(count)
    #     curr -=1
    #     if ((curr + 1) % 10 != 0) and reverseCurr < curr and reverseCurr >= 1:
    #         curr = reverseCurr
    #     print(curr)
    #print ('Case #%d: %d' % (i, numFlips(1,curr)), file=log)
    print ('Case #%d: %d' % (i, numFlips(1,curr)))
