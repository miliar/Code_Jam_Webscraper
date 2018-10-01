#! /usr/bin/env pypy
#
# author: cy7M4KDaktRcoK8aznGukLJpDtI

import sys
import math
import itertools

MP = 4

pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721135  # stop/round at Feynman's point


def solve(args):
    n, k, a = args
    surfmax = 0
    for comb in itertools.combinations(a, k):
        rmax = 0
        surf_ = 0
        for r, h in comb:
            if r > rmax: rmax = r
            surf_ += 2*r*h
        surf = pi*(rmax**2 + surf_)
        if surf > surfmax:
            surfmax = surf
    return surfmax

readin = lambda: sys.stdin.readline().strip()
readinl = lambda: sys.stdin.readline().strip().split()

def getcase():
    n, k = map(int, readinl())
    a = list(map(float, readinl()) for _ in xrange(n))
    return (n, k, a)

n = int(readin())
arglist = (getcase() for _ in xrange(n))

if MP:
    import multiprocessing
    mpool = multiprocessing.Pool(MP)
    reslist = mpool.imap(solve, arglist)
else:
    reslist = (solve(_) for _ in arglist)

for i, r in enumerate(reslist):
    print("Case #{}: {}".format(i+1, r))

