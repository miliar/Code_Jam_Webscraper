#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Jam 2014: Cookie Clicker Alpha

Christopher Davis <http://christopherdavis.me>

Usage:
    python3 solution.py input_file.in > output_file.out
"""

import sys


def readstats(fh):
    return [float(x) for x in fh.readline().strip().split()]


def calccost(cost, cps):
    return cost / cps


def recalc(farmcost, wincost, farmadd, cps):
    tf = calccost(farmcost, cps)
    tw = calccost(wincost, cps)
    twaf = tf + calccost(wincost, cps+farmadd)
    return tf, tw, twaf


def testcase(fh):
    cps = 2
    farmcost, farmadd, towin = readstats(fh)

    counter = 0
    tt_farm, tt_win, tt_win_af = recalc(farmcost, towin, farmadd, cps)
    while tt_win_af < tt_win:
        counter += tt_farm
        cps += farmadd
        tt_farm, tt_win, tt_win_af = recalc(farmcost, towin, farmadd, cps)

    return counter + tt_win


def main(args):
    filename = args[1]
    with open(filename) as fh:
        testcases = int(fh.readline().strip())
        for i in range(1, testcases+1):
            print('Case #{tc}: {ans}'.format(tc=i, ans=testcase(fh)))


if __name__ == '__main__':
    main(sys.argv)
