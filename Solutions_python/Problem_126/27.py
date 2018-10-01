#!/usr/bin/python

def get():
    s, n = raw_input().strip().split()
    n = int(n)

    def isvowels(c):
        return c in 'aeiou'

    ret = 0
    rightest = -1
    lastcount = 0
    for i,x in enumerate(s):
        if not isvowels(x):
            lastcount += 1
            if lastcount >= n:
                ret += i + 2 - n
                rightest = i
                continue
        else:
            lastcount = 0
        if rightest >= 0:
            ret += rightest + 2 - n

    return ret

n = input()
for x in xrange(n):
    print 'Case #%d: %s' % (x+1, get())
