#!/usr/bin/env python2

T = input()
for t in xrange(T):
    s = map(int, list(raw_input().split()[1]))
    answer = 0
    standing = 0
    for i, x in enumerate(s):
        if x != 0 and i > standing:
            answer += i - standing
            standing = i
        standing += x
    print "Case #%d: %d" % (t + 1, answer)
