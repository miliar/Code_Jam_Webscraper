#! /opt/local/bin/python

import sys, itertools, math

def getline(file=sys.stdin):
    return file.readline().strip()

def getints():
    return [int(x) for x in getline().split()]

def rev(s):
    return s[::-1]

def ispal(i):
    s = str(i)
    return s == rev(s)

def split(i):
    s = str(i)
    l = len(s)
    if l % 2:
        mid = s[l / 2]
    else:
        mid = ''
    return (s[0:l / 2], mid)

def incrpal(i):
    if len(str(i)) != len(str(i + 1)):
        return i + 2                    # Special case for 9* => 10*1
    prefix, mid = split(i)
    if mid:
        if mid == '9':
            mid = '0'
            prefix = str(int(prefix or 0) + 1)
        else:
            mid = str(int(mid) + 1)
    else:
        prefix = str(int(prefix) + 1)
    return int(prefix + mid + rev(prefix))

def firstpal(i):
    if ispal(i):
        return i
    prefix, mid = split(i)
    x = int(prefix + mid + rev(prefix))
    while x < i:
        x = incrpal(x)
    return x

def solve(casenum):
    count = 0
    a, b = getints()
    floor = int(math.ceil(math.sqrt(a)))
    ceil = int(math.floor(math.sqrt(b)))
    x = firstpal(floor)
    while x <= ceil:
        if ispal(x * x):
            count += 1
        x = incrpal(x)

    print 'Case #%d: %s' % (casenum, count)

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
