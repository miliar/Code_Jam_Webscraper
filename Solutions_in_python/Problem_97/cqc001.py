#!/usr/bin/python
#
# This script was written by Norio TAKEMOTO 2012-4-13

import re, sys
import numpy as np
import solve_case001 as sol

###############################
#infile=open('input.dat', 'r')
#infile=open('C-small-attempt0.in', 'r')
infile=open('C-large.in', 'r')
#outfile=open('output.dat', 'w')
#outfile=open('C-small-attempt0.out', 'w')
outfile=open('C-large.out', 'w')
###############################






numcase = int(infile.readline())
for jcase in range(numcase):
    line = infile.readline()
    seg = line.split()
    imin = int(seg[0])
    imax = int(seg[1])
    numpair = sol.solve_case(imin, imax)

    outfile.write('Case #%i: %i\n'%(jcase+1, numpair))
    

outfile.close()
