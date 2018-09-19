#!/usr/bin/env python

from sys import stdin, stdout
from fractions import gcd

#def gcd(a, b):
#    if a == 0:
#        return b
#    if a < 0:
#        return gcd(-a, b)
#    if b < a:
#        return gcd(b, a)
#    return gcd(b % a, a)

for c in range(1, int(stdin.readline())+1):
    ti = map(int, str.split(stdin.readline()))
    assert(ti[0] == len(ti) - 1)
    ti = ti[1:]
    T = 0
    for i in range(len(ti) - 1):
        diff = abs(ti[i] - ti[i+1])
        T = gcd(T, diff)
    result = -ti[0] % T;
    stdout.write('Case #%i: %i\n' % (c, result))

