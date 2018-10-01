#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import string

if __name__ == '__main__':
#    file = open('A.in', 'r')
#    file = open('A-small-attempt0.in', 'r')
#    file = open('A-small-attempt1.in', 'r')
    file = open('A-large.in', 'r')
    for i, line in enumerate(file):
        line = line.rstrip()
        if i == 0:
            testCase = int(line)
        else:
            iN = int(line.split(" ")[0])
            iT = int(line.split(" ")[1])
            mini = 2 ** iN
            if (iT + 1) % mini == 0:
                print "Case #" + str(i) + ": ON"
            else:
                print "Case #" + str(i) + ": OFF"                
