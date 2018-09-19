# coding: utf-8

import os, sys, re, string



def main():
    lines = map(lambda x: x.strip(), sys.stdin.readlines())
    cnt = int(lines[0])
    lines = lines[1:]
    def _sort(x,y):
        if x[0] == y[0]:
            return x[1] - y[1]
        return x[0] - y[0]
    for i in range(cnt):
        ttime = int(lines[0])
        ta, tb = map(int, lines[1].split(" "))
        def f(x):
            return 60*int(x[:2]) + int(x[3:])
        def g(x):
            s = x.split(" ")
            return (f(s[0]), f(s[1]) + ttime)
        atimes = map(g, lines[2:2+ta])
        btimes = map(g, lines[2+ta:2+ta+tb])
        atimes.sort(_sort)
        btimes.sort(_sort)
        lines = lines[2+ta+tb:]

        ansa = 0
        ansb = 0

        a_arive = []
        b_arive = []

        while len(atimes) > 0 and len(btimes) > 0:
            if atimes[0][0] < btimes[0][0] or (atimes[0][0] == btimes[0][0] and (len(a_arive) > 0) and atimes[0][0] >= a_arive[0]):
                if len(a_arive) > 0 and a_arive[0] <= atimes[0][0]:
                    a_arive = a_arive[1:]
                else:
                    ansa += 1
                b_arive.append(atimes[0][1])
                b_arive.sort()
                atimes = atimes[1:]
            else:
                if len(b_arive) >0 and b_arive[0] <= btimes[0][0]:
                    b_arive = b_arive[1:]
                else:
                    ansb += 1
                a_arive.append(btimes[0][1])
                a_arive.sort()
                btimes = btimes[1:]

        if len(atimes) > 0:
            for v in atimes:
                if len(a_arive) > 0 and a_arive[0] <= v[0]:
                    a_arive = a_arive[1:]
                else:
                    ansa += 1
        elif len(btimes) > 0:
            for v in btimes:
                if len(b_arive) > 0 and b_arive[0] <= v[0]:
                    b_arive = b_arive[1:]
                else:
                    ansb += 1

        print "Case #%d: %d %d" % (i+1, ansa, ansb)

if __name__ == '__main__':
    main()

