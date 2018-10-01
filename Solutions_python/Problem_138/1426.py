#!/usr/bin/env python

import sys
f = sys.stdin
def readline(): return f.readline().strip()
def readlines(n): return [readline() for _ in xrange(n)]
def readintlines(n): return [readints() for _ in xrange(n)]
def readfloatlines(n): return [readfloats() for _ in xrange(n)]
def readsplit(): return readline().split()
def readint(): return int(readline())
def readfloat(): return float(readline())
def readints(): return map(int, readsplit())
def readfloats(): return map(float, readsplit())

T = readint()

def war(blocks_naomi, blocks_ken):
    blocks_naomi, blocks_ken = blocks_naomi[:], blocks_ken[:]
    points_naomi = 0

    while blocks_naomi:
        block_naomi = blocks_naomi.pop(0)

        # naomi's heaviest > ken's heaviest
        if block_naomi > blocks_ken[0]:
            blocks_ken.pop() # ken plays lightest
            points_naomi += 1

        # naomi's heaviest < ken's heaviest
        else:
            # ken plays lightest block heavier than naomi's block
            block_ken = min(filter(lambda b: b > block_naomi, blocks_ken))
            blocks_ken.pop(blocks_ken.index(block_ken))

    return points_naomi

def deceitfulwar(blocks_naomi, blocks_ken):
    blocks_naomi, blocks_ken = blocks_naomi[:], blocks_ken[:]
    points_naomi = 0

    while blocks_naomi:
        block_naomi = blocks_naomi.pop() # naomi plays lightest

        # naomi's lightest > ken's lightest
        if block_naomi > blocks_ken[-1]:
            blocks_ken.pop() # ken plays lightest
            points_naomi += 1

        # naomi's lightest < ken's heaviest
        else:
            blocks_ken.pop(0) # ken plays heaviest

    return points_naomi

def problem(case):
    readline() # number of blocks
    blocks_naomi, blocks_ken = readfloatlines(2)
    blocks_naomi.sort(reverse=True)
    blocks_ken.sort(reverse=True)
    print 'Case #%i: %s %s' % (case, deceitfulwar(blocks_naomi, blocks_ken),
                               war(blocks_naomi, blocks_ken))

if __name__ == '__main__':
    for case in xrange(1, T+1):
        problem(case)
