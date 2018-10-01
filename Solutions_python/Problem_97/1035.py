#!/usr/bin/env python

Sample = False

def Digits(n):
    if n == 0: return 1
    d = 0
    while n > 0:
        d += 1
        n /= 10
    return d

def Recycled(A, B, n):
    d = Digits(n)
    if d == 1: return 0
    shift = 1
    for cycles in range(1, d): shift *= 10
    count = 0
    m = n
    distinct = set()
    for cycles in range(1, d):
        suffix = m % 10
        radix = m / 10
        m = suffix * shift + radix
        tag = ' '
        if suffix > 0: next
        if (n < m) and (A < m) and (m <= B):
            if m in distinct:
                #print "*DUP*", m
                continue
            distinct.add(m)
            count += 1
            tag = '*'
        #if tag == '*': print n, m, tag, count
    return count

#print Recycled(10000, 99999, 12345)

testCases = int(input())
for no in range(1, testCases+1):
    line = raw_input()
    #print "line", line
    line = line.split()
    #print "new line", line
    values = map(int, line)
    A = values[0]
    B = values[1]
    count = 0
    for n in range(A, B + 1):
        count += Recycled(A, B, n)
    print "Case #%d: %d" % (no, count)
