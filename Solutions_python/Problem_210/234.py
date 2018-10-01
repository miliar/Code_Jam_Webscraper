from random import random
import math
import re
import fractions


# fileio
# fileName = 'B-large'
fileName = 'B-small-attempt1'
# fileName = 'B-test'
input = fileName + ".in"
output = fileName + ".myout"
MOD = 10**9+7

###
with open(input) as fi, open(output, "w") as fo:
    T = fi.readline()
    for count in xrange(int(T)):
        r = 0
        arr = [""] * 1440
        d = {}
        ca = []
        ja = []
        C, J = map(int, fi.readline().strip().split())
        for _ in xrange(C):
            l = map(int, fi.readline().strip().split())
            arr[l[0]] = "C"
            ca.append((l[0], l[1]))
            d[l[0]] = ("C", l[0], l[1])
        for _ in xrange(J):
            l = map(int, fi.readline().strip().split())
            arr[(l[0])] = "J"
            ja.append((l[0], l[1]))
            d[(l[0])] = ("J", l[0], l[1])
        r2 = True
        if len(ca) == 2:
            if (ca[1][1] - ca[0][0]) % 1440 > 720:
                if (ca[0][1] - ca[1][0]) % 1440 > 720:
                    r2 = False
        if len(ja) == 2:
            if (ja[1][1] - ja[0][0]) % 1440 > 720:
                if (ja[0][1] - ja[1][0]) % 1440 > 720:
                    r2 = False
        # shifts = "".join(map(lambda x: d[x][0], sorted(d.keys())))
        # if shifts == "CJCJ" or shifts == "JCJC":
        #     r2 = False
        # print d, shifts
        r = 2 if r2 else 4

        ###
        #normal
        resultStr = "Case #"+str(count+1)+": "+str(r)
        print resultStr
        fo.write(resultStr+'\n')
