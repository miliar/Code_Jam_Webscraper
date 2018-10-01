#!/usr/bin/env python

import sys


def strategy(C, F, X):
    Tfactory = 0
    Tsum = X / 2.0
    k = 0

    while True:
        k += 1

        TfactoryX = Tfactory
        TfactNext = C / (2 + (k - 1) * F)
        Tfactory = TfactoryX + TfactNext

        TsumX = Tsum
        Trest = X / (2 + k * F)
        Tsum = Tfactory + Trest

        if TsumX < Tsum:
            return TsumX


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        (C, F, X) = map(float, line)
        print 'Case #%s: %.7f' % (i + 1, strategy(C, F, X))

main(sys.stdin)
