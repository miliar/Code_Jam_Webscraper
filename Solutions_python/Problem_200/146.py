#!/usr/bin/python

import sys

def solve(n):
    last_dec = None
    for i in xrange(1, len(n)):
        if n[i-1] < n[i]:
            n[i] -= 1
            last_dec = i
    if last_dec:
        for i in xrange(0, last_dec):
            n[i] = 9
    return n

def deconstruct(n):
    return list(reversed([int(x) for x in str(n)]))

def reconstruct(n):
    return int("".join(str(x) for x in reversed(n)))

def main():
    T = next(sys.stdin)
    for t, line in enumerate(sys.stdin, 1):
        print "Case #{}: {}".format(t, reconstruct(solve(deconstruct(line.strip()))))

main()

