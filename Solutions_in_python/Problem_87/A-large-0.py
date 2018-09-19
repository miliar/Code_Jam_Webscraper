#!/usr/bin/env python

from sys import stdin

def main():
    T = int(stdin.readline())
    for j in range(T):
        X, S, R, t, N = map(int, stdin.readline().split())
        dist = 0
        walkways = []
        for i in range(N):
            Bi, Ei, wi = map(int, stdin.readline().split())
            d = Ei - Bi
            dist += d
            walkways.append((float(wi), d))
        walkways.append((0.0, X - dist))
        walkways = sorted(walkways)
        time = 0
        for w, d in walkways:
            ts = d / (w + S)
            tr = d / (w + R)
            if t >= tr:
                time += tr
                t -= tr
            elif t > 0:
                time += t + (d - t * (w + R)) / (w + S)
                t = 0
            else:
                time += ts
        print "Case #{0}: {1}".format(j+1, time)

main()
