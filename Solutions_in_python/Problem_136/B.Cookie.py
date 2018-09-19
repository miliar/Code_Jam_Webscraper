#!/usr/bin/python

from decimal import *
getcontext().prec = 100
import sys

def process(C, F, X):
    Fp = Decimal(2.0)
    T = Decimal(0.0)
    A_cur = Decimal(X / Fp)
    A_next = Decimal(X / (F + Fp))
    B = Decimal(C / Fp)
    while A_cur > (B + A_next):
        T += B
        Fp += F
        A_cur = A_next
        A_next = X / (F + Fp)
        B = Decimal(C / Fp)

    T += X / Fp
    return round(T, 7)


fin = open(sys.argv[1], 'r')

fout = open(sys.argv[1].split(".")[0] + ".out", "w")

nb_cases = int(fin.readline())

for i in range(1, nb_cases + 1):
    line = fin.readline().strip().split(" ")
    C_ = Decimal(line[0])
    F_ = Decimal(line[1])
    X_ = Decimal(line[2])
    print "Case #%d" % (i)
    fout.write("Case #%d: %s\n" % (i, process(C_, F_, X_)))

fout.flush()
fout.close()
fin.close()
