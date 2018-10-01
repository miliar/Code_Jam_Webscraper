import heapq
import itertools
import math
import re
import string
import sys

def tobase(n, base):
    s = ""
    while n > 0:
        s += str(n % base)
        n = n // base
    return s

def ishappy(n, base):
#    seen = set(n)
#    while True:
#        if n == "1": return True
#        n = tobase(sum(map(lambda x: int(x, base) * int(x, base), n)), base)
#        if n in seen: return False
    for i in range(50):
        if n == "1": return True
        n = tobase(sum(map(lambda x: int(x, base) * int(x, base), n)), base)
    return False

t = int(sys.stdin.readline())
for i in range(t):
    bases = map(int, sys.stdin.readline().split())
    sys.stderr.write(str(i))
    j = 2
    while True:
        if all(ishappy(tobase(j, b), b) for b in bases):
            break
        j += 1
    print "Case #%d: %d" % (i + 1, j)
