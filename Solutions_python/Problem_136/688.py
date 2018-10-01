#!/usr/bin/python

ifn = 'sample.in'
ofn = 'sample_ans.txt'

ifn = 'B-small-attempt0.in'
ofn = 'B-small-ans.txt'

ifn = 'B-large.in'
ofn = 'B-large-ans.txt'

ofp = open(ofn, 'w')

with open(ifn, 'r') as ifp:
        T = (int)(ifp.readline())
        for i in range(T):
                line = ifp.readline()
                C, F, X = [float(p) for p in line.split(' ')]
                R = 2
                
                if X < C:
                        time = X/R
                else:
                        time = 0
                        while(R < F*(X/C - 1)):
                                time = time + C/R
                                R = R + F
                        time = time + X/R
                        
                ofp.write("Case #%d: %.7f\n" % (i+1, time))
ifp.close()
ofp.close()
