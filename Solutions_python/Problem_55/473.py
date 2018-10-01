#!/usr/bin/env python
#-*- coding:utf-8 -*-

from itertools import repeat

def main():
    fName = 'C-small-attempt0'
    fIn = open(fName+'.in', 'r')
    fOut = open(fName+'.out', 'w')
  
    t = int(fIn.readline().strip())

    for i in xrange(t):
        r, k, n = map(int, fIn.readline().strip().split(' '))
        q1 = map(int, fIn.readline().strip().split(' '))
        result = 0

        for j in xrange(r):
            s = k
            q2 = []
            while len(q1) and q1[0] <= s:
                result += q1[0]
                s -= q1[0]
                q2.append(q1.pop(0))
            q1.extend(q2)
                
        fOut.write('Case #%s: %s\n' % (i + 1, result))
                
if __name__ == '__main__': main()