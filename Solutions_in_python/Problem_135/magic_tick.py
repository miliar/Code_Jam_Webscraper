#!/usr/bin/env python
import sys
from optparse import OptionParser
from collections import deque
usage = "usage: %prog input"
parser = OptionParser(usage=usage)
(options, args) = parser.parse_args()
if args:
    if args[0] == "-":
        f = sys.stdin
    else:
        f = open(args[0])
else:
    parser.error("Need input from file or stdin")

T = int(f.readline())

def find_row():
    pos1 = int(f.readline())
    arr1 = []
    for i in range(0,4):
        arr1.append(set(f.readline().split()))
    return arr1[pos1-1] 

for i in range(1,T+1):
    value = list(find_row() & find_row())
    count = len(value)
    print 'Case #%s:' % i,
    if count > 1:
	print 'Bad magician!'
    elif count == 1:
	print value.pop()
    else:
        print 'Volunteer cheated!'

