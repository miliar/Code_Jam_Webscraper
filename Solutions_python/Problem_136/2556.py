#!/usr/bin/python2
# -*- coding: utf8 -*-
# Google Code Jam 2014 - Qualification Round - Problem B - Mateusz Kurek


def solve_case():
    c, f, x = map(float, raw_input().split(' '))
    w = 0
    p = x / 2
    farms = 0
    while True:
        current = w + c / (2 + farms * f)
        current_p = current + (x / (2 + (farms + 1) * f))
        if p > current_p:
            p = current_p
            w = current
        else:
            break
        farms += 1
    return p


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        print("Case #{0}: {1:.7f}".format(i, solve_case()))

if __name__ == '__main__':
    main()
