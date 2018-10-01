# -*- coding: utf-8 -*-
import re, sys

def coreCalc(data):
    n = data[0]
    s = data[1]
    p = data[2]
    scores = data[3:]
    result = 0
    for i in scores:
        if (i == 0) and (p != 0):
            continue
        avg = i / 3
        high = avg
        if (i - avg * 3 > 0):
            high = avg + 1
        if high >= p:
            result += 1
        else:
            if (s == 0):
                continue
            if (avg * 3 == i):
                high = avg + 1
                if (high >= p):
                    result += 1
                    s -= 1
            elif (avg * 3 + 2 ==i):
                high = avg + 2
                if (high >= p):
                    result += 1
                    s -= 1
    return result
    
N = int(sys.stdin.readline().strip())
for qw in range(1, N + 1):
    print 'Case #%d:' % qw,

    data = [int(i) for i in sys.stdin.readline().strip().split()]
    result = coreCalc(data)
    print result
