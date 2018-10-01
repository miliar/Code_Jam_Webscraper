#! /usr/bin/env python


import sys


def main():
    testcases = int(sys.stdin.readline())

    for i in xrange(testcases):
        blockcount = int(sys.stdin.readline())

        nb = map(float, sys.stdin.readline().strip().split(' '))
        kb = map(float, sys.stdin.readline().strip().split(' '))

        print "Case #%d: %d %d" % (i+1, dwar(nb,kb), war(nb,kb))

def war(nb, kb):
    nscore = 0

    nb = sorted(nb, reverse=True)
    kb = sorted(kb, reverse=True)

    while len(nb) > 0:
        n = nb.pop(0)
        if n > kb[0]:
            kb.pop()
            nscore += 1
        else:
            x = 0
            while x < len(kb) and kb[x] > n:
                x += 1
            x -= 1
            kb.pop(x)

    return nscore


def dwar(nb, kb):

    nscore = 0
    nb = sorted(nb)
    kb = sorted(kb)

    while len(nb) > 0:
        if kb[0] > nb[0]:
            nb.pop(0)
            kb.pop()
        else:
            nb.pop(0)
            kb.pop(0)
            nscore += 1

    return nscore


main()
