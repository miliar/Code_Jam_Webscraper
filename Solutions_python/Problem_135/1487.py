#!/usr/bin/env python

import sys
f = sys.stdin
def readline(): return f.readline().strip()
def readlines(n): return [readline() for _ in xrange(n)]
def readintlines(n): return [readints() for _ in xrange(n)]
def readsplit(): return readline().split()
def readint(): return int(readline())
def readints(): return map(int, readsplit())

T = readint()

def case(n):
    result = None
    answer1 = readint()
    arrangement1 = readintlines(4)
    answer2 = readint()
    arrangement2 = readintlines(4)

    row1 = arrangement1[answer1-1];
    row2 = arrangement2[answer2-1];

    card = None
    for c in row1:
        if c in row2:
            if card is None:
                card = c
            else:
                result = 'Bad magician!'
                break
    else:
        result = card

    if card is None:
        result = 'Volunteer cheated!'

    print 'Case #%i: %s' % (n, result)

if __name__ == '__main__':
    for n in xrange(1, T+1):
        case(n)
