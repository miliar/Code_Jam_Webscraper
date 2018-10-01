#!/usr/bin/python

def get():

    def read():
        r = input()
        row = [raw_input().strip() for x in xrange(4)][r-1]
        return set(map(int, row.split()))

    s = read() & read()
    if len(s) == 0:
        return 'Volunteer cheated!'
    if len(s) > 1:
        return 'Bad magician!'
    for x in s:
        return x

t = input()
for x in xrange(t):
    print 'Case #%d: %s' % (x+1, get())
