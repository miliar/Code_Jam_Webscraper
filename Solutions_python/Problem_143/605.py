#!/usr/bin/python
#
# This script was written by Norio TAKEMOTO 2014-5-4.

##################################
#infname='input_sample.dat'
#outfname='output_sample.dat'
infname='B-small-attempt0.in'
outfname='output_smallB.dat'
##################################


def solve_small(A, B, K):

    npair=0
    for aa in range(A):
        for bb in range(B):
            if K>(aa&bb):
                npair+=1
    return npair


infile=open(infname,'r')
numcaseT=int(infile.readline())
list_A=[]
list_B=[]
list_K=[]
for jcase in range(numcaseT):
    seg=infile.readline().split() 
    list_A.append(int(seg[0]))
    list_B.append(int(seg[1]))
    list_K.append(int(seg[2]))
infile.close()

outfile=open(outfname,'w')
for jcase in range(numcaseT):
    answer=solve_small(list_A[jcase], list_B[jcase], list_K[jcase])
    outfile.write('Case #%i: %i\n'%(jcase+1, answer))

outfile.close() 
