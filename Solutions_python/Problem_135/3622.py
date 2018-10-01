#!/usr/bin/env python
import sys
n = int(sys.stdin.readline())
for i in range(n):
    guess1 = int(sys.stdin.readline())
    lines1 = [set(sys.stdin.readline()[:-1].split(' ')) for j in range(4)]
    guess2 = int(sys.stdin.readline())
    lines2 = [set(sys.stdin.readline()[:-1].split(' ')) for j in range(4)]
    r1 = lines1[guess1-1]
    r2 = lines2[guess2-1]
    result = r1 & r2
    l = len(result)
    s = 'Volunteer cheated!' if (l == 0) else list(result)[0] if (l == 1) else 'Bad magician!'
    print "Case #%d: %s" % (i+1, s)
