#!/usr/bin/python

import array
import sys


class snapper:
    def __init__(self, power = False):
        self._powered = False
        self._enabled = power

    def snap(self):
        if self._powered:
            self._enabled = not self._enabled

    def output(self):
        return (self._powered and self._enabled)
    def power(self, power):
        self._powered = power


def simulate(N, K):
    snappers = []
    for i in range(0,N):
        snap = snapper()
        snappers.append(snap)
    snappers[0].power(True)

    for i in range(0,K):
        for j in range(0,N):
            snappers[j].snap()
        for j in range(0,N-1):
            snappers[j+1].power(snappers[j].output())
        #line = ""
        #for j in range(0,N):
        #    line += str(snappers[j].output()) + " "
        #print line

    return snappers[N-1].output()


T = int(sys.stdin.readline())

for s in range(0,T):
    line = sys.stdin.readline()
    items = line.split()
    K = int(items[1])
    N = int(items[0])
    light = simulate(N, K)
    if light:
        text = "ON"
    else:
        text = "OFF"
    print "Case #" + str(s+1) + ": " + text

