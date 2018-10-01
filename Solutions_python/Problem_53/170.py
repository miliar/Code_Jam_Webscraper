#!/usr/bin/python

T = int(raw_input())

for i in range(T):
    N, K = (int(v) for v in raw_input().split(' '))
    on = not (K + 1) % (2 ** N)
    print "Case #%d: %s" % (i + 1, "ON" if on else "OFF")
