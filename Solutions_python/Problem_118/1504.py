#!/usr/bin/python
import readline
root = [1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001, 1010101, 1011101, 1012101, 1100011, 1101011, 1102011, 1110111, 1111111, 2000002, 2001002]
square = []
for i in root:
    square.append(i*i)

def getIndex(n):
    bit = 1 << 8
    r = 0
    while True:
        bit >>= 1
        if bit == 0:
            break
        t = r | bit
        try:
            if square[t] <= n:
                r = t
        except IndexError:
            pass
    return r

def getIndexExclude(n):
    if (n <= 1):
        return -1
    bit = 1 << 8
    r = 0
    while True:
        bit >>= 1
        if bit == 0:
            break
        t = r | bit
        try:
            if square[t] < n:
                r = t
        except IndexError:
            pass
    return r

cases = int(raw_input())
for case in xrange(1, cases+1):
    a, b = (int(x) for x in raw_input().split())
    print "Case #%d: %d" % (case, getIndex(b) - getIndexExclude(a))
