#! /usr/bin/env python
# -*- coding: UTF-8 -*-

''' A
'''

import sys, math, random

########################################################################

def replaceBlueRed(tbl):
    ret,p = '',True
    for y,r in enumerate(tbl):
        if ret:
            ret += "\n"
        for x,c in enumerate(r):
            if c=='#' and y<len(tbl)-1 and x < len(tbl[0])-1 and tbl[y][x+1]=='#' and tbl[y+1][x]=='#' and tbl[y+1][x+1]=='#':
                tbl[y][x],tbl[y][x+1],tbl[y+1][x],tbl[y+1][x+1] = '/','\\','\\','/'
            ret += tbl[y][x]
            if tbl[y][x] == '#':
                p = False
    return ret,p

def solve(fc):
    T = int(fc[0])

    k = 1
    for i in range(T):
        l1 = fc[k].strip()
        R,C = map(lambda x:int(x), l1.split(' '))

        tbl = [[0 for j in range(C)] for jj in range(R)]
        for j in range(R):
            k += 1
            tbl[j] = [ c for c in fc[k].strip() ]
        
        ret,p = replaceBlueRed(tbl)
        
        print 'Case #%i:'%(i+1)
        if not p:
            print 'Impossible'
        else:
            print ret
        
        k += 1

########################################################################

import unittest

class UT1(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(True,True)

########################################################################

assert len(sys.argv) > 1, 'args!'
fn = sys.argv[1]
fc = open(fn).readlines()

v = '-v' in sys.argv

if '--test' in sys.argv:
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(UT1))
else:
    solve(fc)
