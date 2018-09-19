#!/usr/bin/env python

import math, sys
def solve():
    lettersmax_s,keysmax_s,alphabetsize_s=(s for s in inputfile.readline().split())
    freq_s=inputfile.readline().split()
    lettersmax=int(lettersmax_s)
    keysmax=int(keysmax_s)
    alphabetsize=int(alphabetsize_s)
    if alphabetsize>lettersmax*keysmax: return 'Impossible'
    freq=[]
    for s in freq_s:
        freq.append(int(s))
    freq=sorted(freq,reverse=True)
    #keysarray=[0 for i in range(keysmax)]
    presses=0
    for i in range(len(freq)):
        presses+=freq[i]*(i/keysmax+1)
    return str(presses)

letter,set='A','large'
file='C:/Documents and Settings/brunoff/My Documents/My Code/'+letter+'1C-code/'+letter+'-'+set
inputfile=open(file+'.in','r')
outputfile=open(file+'.out','w')

cases = int(inputfile.readline())
for case in range(cases):
    output='Case #%d: %s'%(case+1,solve())
    print output
    outputfile.write(output+'\n')

inputfile.close()
outputfile.close()