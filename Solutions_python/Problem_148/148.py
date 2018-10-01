#!/usr/bin/python

import sys;
import os.path; 
from collections import *;
from Queue import *;
from array import array;

def readi():
    return int(sys.stdin.readline().strip());

def readia():
    return [int(x) for x in sys.stdin.readline().strip().split()];

def readfa():
    return [float(x) for x in sys.stdin.readline().strip().split()];

def reads():
    return sys.stdin.readline().strip();

def main():
    nt = readi();
    for t in range(1, nt+1):
        (N, X) = readia();
        sz = readia();
        if len(sz) != N:
            print >>sys.stderr, "BAD!!! t = ", t;
        sz.sort(cmp = lambda x, y: cmp(y, x));


        numDisks = 0;

        first = 0;
        last = len(sz) - 1;
        while first <= last:
            numDisks += 1;
            sizeLeft = X - sz[first];
            if last > first and sz[last] <= sizeLeft:
                last -= 1;
            first += 1;


        #print sz;
        #aa = array('i');
        #aa.fromlist(sz);
        #print aa;

        #first = 0;
        #last = len(aa) - 1;
        #while first < len(aa):
        #    ++numDisks;
        #    sizeLeft = X - aa[


        print "Case #%d: %d" % (t, numDisks);
    

main();
