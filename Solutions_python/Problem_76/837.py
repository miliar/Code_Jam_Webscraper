# -*- coding: utf-8 -*-

import sys

bin = lambda n : (n > 0) and (bin(n/2) + str(n%2)) or '' 

def patrickadd(b1, b2):
    result = ''

    b1len = len(b1)
    b2len = len(b2)
    maxlen = b1len
    if (b1len > b2len):
        b2 = b2.zfill(b1len)
    if (b2len > b1len):
        b1 = b1.zfill(b2len)
        maxlen = b2len
    for i in range(0, maxlen):
        if b1[i] == b2[i]:
            result += '0'
        else:
            result += '1'

    return result

def patricksum(pienumbers):
    result = ''
    for number in pienumbers:
        result = patrickadd(result, bin(number))
    return int(result, 2)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T+1):
    crying = True
    maxvalue = 0
    N = int(fin.readline())
    numbers = [int(x) for x in fin.readline().split(" ")]
    for i in range(0, N + 1):
        for pieces in range(0, N - i):
            if pieces + 1 <> N:
                #print "start at %d, %d pieces" % (i, pieces + 1)
                #print "pie1: %s, pie2: %s" % (numbers[i:i + pieces + 1], numbers[0:i] + numbers[i + pieces + 1:])
                #print "pie1 sum: %s, pie2 sum: %s" % (patricksum(numbers[i:i + pieces + 1]), patricksum(numbers[0:i] + numbers[i + pieces + 1:]))
                if patricksum(numbers[i:i + pieces + 1]) == patricksum(numbers[0:i] + numbers[i + pieces + 1:]):
                    maxvalue = max(maxvalue, sum(numbers[i:i + pieces + 1]), sum(numbers[0:i] + numbers[i + pieces + 1:]))
                    crying = False
                    #print maxvalue
        pass
    if crying:
        print "Case #%d: NO" % case
    else:
        print "Case #%d: %d" % (case, maxvalue)
