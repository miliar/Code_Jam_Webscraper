from sys import stdin
from fractions import Fraction
import fractions

def riadok():
    return map(int, stdin.readline().split())

for cas in range(int(stdin.readline())):
    a = riadok()[1:]
    a.sort()
    d = a[1] - a[0]
    for i in range(1, len(a)):
        d = fractions.gcd(d, a[i] - a[0])
    print "Case #%d: %d" % (cas + 1, (-a[0]) % d)
