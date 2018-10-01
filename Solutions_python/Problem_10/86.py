import sys
import math
import os, os.path
from file_access import open_file, cnum



def problem_testcase(fin, fout, t):
    P, K, L = [int(x) for x in fin.readline().strip().split()]
    freqs = [(key, int(fr)) for key, fr in enumerate(fin.readline().strip().split())]
    
    
    #print P, K ,L
    #print freqs
    s_freqs = sorted(freqs, key=lambda item:-item[1])
    #print s_freqs
    if(P*K < L):
        return ('Impossible',)
    
    
    presses = 0
    assigned = 0
    factor = 1
    for key, fr in s_freqs:
        presses += factor*fr
        assigned += 1
        if assigned % K == 0:
            factor += 1
    
    
    return (presses,)









    
if __name__=='__main__':
    open_file(__file__)
    
    
    

    

