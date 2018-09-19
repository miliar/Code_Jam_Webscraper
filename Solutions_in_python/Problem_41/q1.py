#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 順列を格納するリスト

def parseQ(file='test'):
    f = open(file)
    line = f.readline()
    T_total = int(line)

    for tnum in range(T_total):
        digi = []
        vals = int(f.readline()[:-1])
        val = vals
        while vals > 0:
            digi.append(vals % 10)
            vals = vals // 10
        digi.sort()
        i = 0
        for x in digi:
            if x == 0:
                i += 1
                continue
            else:
                i = digi.index(x)
                break
        #makeList(digi, i, val)
        global suchi
        make_perm(len(digi), digi)
        j = suchi.index(val)
        while 1:
            if j == len(suchi) - 1:
                digi.append(0)
                digi.sort()
                suchi = []
                make_perm(len(digi), digi)
                k = 10 ** (len(digi) - 1)
                s2 = [x for x in suchi if x >= k]
                j = suchi.index(val)
                print "Case #%d: %d" % (tnum + 1, s2[0])
                break
            else:
                j += 1
                if suchi[j] > val:
                    print "Case #%d: %d" % (tnum + 1, suchi[j])
                    break
                

perm = []
suchi = []

# 順列の生成
def make_perm(n, digi, m = 0):
    if n == m:
        v = makeNumber(digi)
        suchi.append(makeNumber(digi))
    else:
        for x in range(1, n + 1):
            if x in perm:
                continue
            perm.append(x)
            make_perm(n, digi, m + 1)
            perm.pop()
                                                
def makeNumber(digi):
    v = 0
    for x in perm:
        v = v * 10 + digi[x - 1]
    return v


if __name__ == '__main__':
    parseQ(sys.argv[1])
