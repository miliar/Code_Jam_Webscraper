# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:00:45 2017

@author: Bert
"""


"""
4
4 4
1.4000
0.5000 0.7000 0.8000 0.6000
2 2
1.0000
0.0000 0.0000
"""

def mult(l):
    r = 1
    for i in l:
        r *= i
    return r

def handle_case(cores,needcores,TU,perf):
#    if needcores < cores:
#        s= sorted(perf, reverse=True)
#        perf = s[:needcores] #should be enough for next data set
#        remainder = s[needcores:]
    if sum(perf)+TU == len(perf):
        return 1.0
    
    #just maximize it in ints first, then we divide at the end
    p = [i*10000 for i in perf]
    TUK = TU*10000
    
    while TUK > 0:
        pset = set(p)
        m = min(pset)
        k = p.count(m)
        pset.remove(m)
        credit = TUK
        if len(pset) > 0:
            mnext = min(pset)
            if k*(mnext-m) < TUK:
                credit = k*(mnext-m)        
        
        to_add = credit / k
        for q in range(k):
            pos = p.index(m)
            p[pos] += to_add
        TUK -= credit
    

    p = [i/10000 for i in p]
    return mult(p) 
    

def read_case(ifh,ofh):
    N,K = ifh.readline().split()
    U = float(ifh.readline())
    Ps = list(map(float,ifh.readline().split()))
    solution = handle_case(int(N),int(K),U,Ps)
    o = "Case #{}: {}".format(x+1,solution)
    print (o)
    ofh.write(o)
    ofh.write("\n")
    
with open("C-small-1.in") as fh, open("C1output-small.txt","w") as op:
#with open("C-large.in") as fh, open("Coutput-large.txt","w") as op:
#with open("Ctest.txt") as fh, open("Coutput-test.txt","w") as op:
    cases = int(fh.readline())
    for x in range(cases):
        read_case(fh,op)