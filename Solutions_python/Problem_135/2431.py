#!/usr/bin/env python2

T = input()

for TT in range(1, T + 1):
    print "Case #%d:" % (TT),
    A1 = input()
    VV = []
    for K in range(4):
        VV.append(raw_input().split(' '))
    A2 = input()
    WW = []
    for K in range(4):
        WW.append(raw_input().split(' '))
    VVV = set(VV[A1 - 1])
    WWW = set(WW[A2 - 1])
    RES = VVV.intersection(WWW)
    if len(RES) == 1:
        print RES.pop()
    elif len(RES) > 1:
        print 'Bad magician!'
    else:
        print 'Volunteer cheated!'
