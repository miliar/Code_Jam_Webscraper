#!/usr/bin/env python
import numpy as np
import scipy as sp
import os
import sys

def get_result(smax,sarr):
    shynessarr = np.array(list(sarr)).astype(int)
    result = 0
    sumclapps = (shynessarr[0])
    print 'start',smax, shynessarr
    for i in xrange(1,smax+1):
        print i,result,sumclapps,shynessarr[i]
        if shynessarr[i]==0:
            continue
        if sumclapps>=i: 
            sumclapps+=(shynessarr[i])
            continue
        else:
            result+=i-sumclapps
            sumclapps+=(i-sumclapps)+shynessarr[i]
    return result


def main(infile):
    fin=open(infile,mode='r')
    fout = open("test_output.txt",mode='w')
    ncase = int(fin.readline())
    for i in xrange(ncase):
        line = fin.readline()
        smax = int(line.split()[0])
        sarr = (line.split()[1])
        result = get_result(smax,sarr)
        fout.write("Case #%d: %d\n" % ((i+1),result))
    fin.close()
    fout.close()
    return
if __name__=='__main__':
    main(sys.argv[1])
