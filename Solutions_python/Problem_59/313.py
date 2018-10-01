#!/bin/python
#import sys
#sys.stdin = file("sample.in")
from os.path import normpath,join


def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def makeparents(d):
    ret = [d]
    parent = d
    while parent != "/":
        parent = normpath(join(parent,".."))
        ret.append(parent)
    return sorted(ret)

def appendparent(dirs):
    ret = set(dirs)
    for d in dirs:
        parent = d
        while parent != "/":
            parent = normpath(join(parent,".."))
            ret.add(parent)
    return ret

def solve(exists, wants):
    exists = appendparent(exists)
    ret = 0
    for want in wants:
        for need in makeparents(want):
            if need not in exists:
                ret += 1
                exists.add(need)
    return ret

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        N,M = tuple(readints())
        exists = set([ raw_input() for x in range(N) ] + ["/"])
        wants = set([ raw_input() for x in range(M) ])

        print "Case #%d: %s" % ( i+1, solve(exists,wants))
