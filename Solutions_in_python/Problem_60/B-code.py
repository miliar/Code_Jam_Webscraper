import sys,collections
import os,re

#NAME = 'B-example'
#NAME = 'B-small-attempt0'
NAME = 'B-large'

BASEDIR = os.path.expanduser('~/Projects/Challenge/Google CodeJam/GCJ 2010 Round 1B/%s')
inname  = BASEDIR % (NAME + '.in')
outname = BASEDIR % (NAME + '.out')

with open(inname) as fin:
    with open(outname,'w') as fout:
        num_cases = int(fin.readline())
        for case_idx in range(1,1+num_cases):
            N,K,B,T = map(int,fin.readline().split())
            X = map(int,fin.readline().split())
            V = map(int,fin.readline().split())
            assert len(X) == len(V) == N
            # real work here!

            Z = "".join( '01'[x+v*T >= B] for x,v in zip(X,V) )
            if Z.count('1') < K:
                answer = 'IMPOSSIBLE'
                Y = None
            else:
                Y=Z
                for i in range(Z.count('1')-K):
                    Y = Y[1+Y.index('1'):]
                y = Y.count('0')
                answer = `sum(x.start() for x in re.finditer('0', Y))-y*(y-1)/2`
            #print Z, Y, K, answer
                
            print >> fout, "Case #%d: %s" % (case_idx, answer)
