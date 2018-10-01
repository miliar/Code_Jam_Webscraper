#!/usr/bin/env python
# -*- coding: UTF-8 -*-


FILE = 'B-large.in'

lines = []
for line in file(FILE).readlines():
    lines += [line.replace("\r", "").replace("\n", "").replace("\t", "")]


def check(O, D, time):
    o, d = len(O)-1, len(D)-1
    subtractor = 0
    ot = False
    if len(O) == 0 or len(D) == 0:
        return subtractor
    O.sort(), D.sort()
    while o >= 0:
        if O[o] >= D[d] + time:
            O.pop(o), D.pop(d)
            o -= 1
            d = len(D)-1
            subtractor -= 1
        else:
            d -= 1
        if d < 0:
            d = len(D)-1
            o -= 1
        if len(D) == 0 or len(O) == 0:
            return subtractor
    return subtractor

def get_trains(Ao, Ad, Bo, Bd, time):
    na = len(Ao) + check(Ao, Bd, time)
    nb = len(Bo) + check(Bo, Ad, time)
    return na, nb

tests = int(lines.pop(0))

for i in range(tests):
    time = int(lines.pop(0))
    ab = lines.pop(0).split(" ")
    a, b = int(ab[0]), int(ab[1])
    Ao, Ad = [], []
    for j in range(a):
        l = lines.pop(0).split(" ")
        o = l[0].split(":")
        o = int(o[0])*60 + int(o[1])
        d = l[1].split(":")
        d = int(d[0])*60 + int(d[1])
        Ao += [o]
        Ad += [d]
    Bo, Bd = [], []
    for j in range(b):
        l = lines.pop(0).split(" ")
        o = l[0].split(":")
        o = int(o[0])*60 + int(o[1])
        d = l[1].split(":")
        d = int(d[0])*60 + int(d[1])
        Bo += [o]
        Bd += [d]
    #print a, b, Ao, Ad, Bo, Bd
    a, b = get_trains(Ao, Ad, Bo, Bd, time)
    print "Case #%d: %d %d"%(i+1, a, b)
