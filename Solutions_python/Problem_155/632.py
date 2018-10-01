#!/usr/bin/env python

def solve_case(s):
    standing = 0
    additional = 0
    for i in xrange(len(s)):
        if s[i] > 0:
            if standing < i:
                additional += i - standing
                standing = i
            standing += s[i]
    return additional

T = int(raw_input())
for t in xrange(T):
    s = raw_input().rstrip().split()[1]
    s = [int(x) for x in s]
    print "Case #%d: %d" % (t+1, solve_case(s))
