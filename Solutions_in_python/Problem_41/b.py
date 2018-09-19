#!/usr/bin/env python
import sys
import re
import pdb

def printer(result, num):
    print 'Case #%d: %d' % (num, result)
    
def defaultdict():
    return {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    }

def counteddict(number):
    ret = defaultdict()
    for key in ret:
        result = re.findall(key, number)
        ret[key] = len(result)
    return ret

f = open (sys.argv[1], 'r')
T = int(f.readline())

content = f.readlines()

for i, number in enumerate(content): 
    currentdict = counteddict(number)
    inumber = int(number)
    nextnum = inumber + 1
    while True:
        if (inumber % 10) == 0:
            tmp = inumber
            while tmp % 10 == 0:
                tmp = tmp / 10
            if tmp == 1:
                printer(inumber*10, i+1)
                break
        if inumber < 10:
            printer(inumber * 10, i+1)
            break
        newdict = counteddict(str(nextnum))
        if newdict == currentdict:
            printer(nextnum, i+1)
            break
        nextnum += 1

