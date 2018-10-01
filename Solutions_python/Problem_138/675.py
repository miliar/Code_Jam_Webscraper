#!/usr/bin/env python
#coding=utf-8
import copy

##inPath = 'test.in'
##outPath = 'test.out'
##inPath = 'D-small-attempt0.in'
##outPath = "D-small-attempt0.out"
inPath = 'D-large.in'
outPath = "D-large.out"

def DeceitfulWar(naomi, ken):
    nBox = copy.deepcopy(naomi)
    kBox = copy.deepcopy(ken)
    nBox.sort()
    kBox.sort()
    naomiPoint = 0
    while len(kBox) != 0:
        if nBox[-1] > kBox[-1]:
            naomiPoint += 1
            nBox.pop()
        else:
            nBox = nBox[1:]
        kBox.pop()
    
    return naomiPoint

def War(naomi, ken):
    nBox = copy.deepcopy(naomi)
    kBox = copy.deepcopy(ken)
    nBox.sort()
    kBox.sort()
    naomi.sort()
    naomiPoint = 0
    for num in naomi:
        if num > max(kBox):
            break
        else:
            for index in xrange(len(kBox)):
                if kBox[index] > num:
                    t = kBox[index]
                    kBox.remove(t)
                    naomiPoint += 1
                    break
    return len(ken) - naomiPoint


with open(outPath,'w') as outf:
    with open(inPath) as inf:
        n = int(inf.readline().strip()) 
        for case in xrange(1, n+1):
##            print case
            inf.readline()
            naomi = [float(i) for i in inf.readline().strip().split()]
            ken = [float(i) for i in inf.readline().strip().split()]
            outf.write("Case #" + str(case) + ": " \
                       + str(DeceitfulWar(naomi, ken)) + ' ' \
                       + str(War(naomi, ken)) + '\n')
    inf.close()
outf.close()
