#!/usr/bin/python

from numpy import *

import os
import sys
import math

if len(sys.argv) < 2:
    print "Usage: ./snapper.py <inputfile>"
    sys.exit(0)

inputFile = sys.argv[1]
input = fromfile (inputFile, int, -1, " ")
num = input[0]
for i in range(num):
    n = input[i*2+1]
    k = input[i*2+2]
    nraised2m1 = (1 << n) - 1
    if (nraised2m1 & k == nraised2m1):
        res = "ON"
    else:
        res = "OFF"
    print "Case #" + str(i+1) + ": " + res 
