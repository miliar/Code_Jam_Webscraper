#!/usr/bin/python
import sys

if len(sys.argv) < 2:
    print 'missing argument'
    exit()

f = open(sys.argv[1], 'r')
casesTotal = int(f.readline())
casesCurrent = 1;
while casesCurrent <= casesTotal:
    n = int(f.readline().strip())
    values = map(int, f.readline().strip().split())
    numHits = 0
    i = 1
    while i <= n:
        if i != values[i - 1]:
            numHits += 1
        i += 1
    print 'Case #%d: %.6f' % (casesCurrent, numHits);
    casesCurrent += 1;
