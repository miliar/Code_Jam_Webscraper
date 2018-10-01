#!/usr/bin/python

import sys


def opposer(opposed, lst):
    o = lst[-1]
    for (a, b) in opposed:
        if a == o:
            if b in lst:
                return []

        if b == o:
            if a in lst:
                return []
    return lst

def combiner(combine, lst):
    if len(lst) < 2: return lst
    for c in combine:
        if set(lst[-2:]) == set(c[0:2]):
            lst[-2:] = c[2]
            lst = combiner(combine, lst)
            break
    return lst

def getSolution(combiners, opposers, invoked):
    w = []
    for c in invoked:
        w.append(c)
        w = combiner(combiners, w)
        w = opposer(opposers,w)

    return "[" + ", ".join(w) + "]"

#print getSolution([],[],"EA")
#print getSolution([('Q','R','I')],[], "RRQR")
#print getSolution([('Q','F','T')],[('Q', 'F')], "FAQFDFQ")
#print getSolution([('E','E','Z')],[('Q', 'E')], "QEEEERA")
#print getSolution([],[('Q', 'W')], "QW")

caseNum = 1

file = open(sys.argv[1], "r")
file.readline()
line = file.readline()

while line:
    line = line.strip().split()
    nc = int(line[0])
    no = int(line[nc+1])
    combs = line[1:nc+1]
    opps = line[nc+2:-2]
    print "Case #%d: %s" % (caseNum, getSolution(combs, opps, line[-1]))
    line = file.readline()
    caseNum += 1
