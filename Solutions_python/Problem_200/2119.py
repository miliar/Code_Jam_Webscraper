#https://code.google.com/codejam/contest/3264486/dashboard#s=p1
import os
import math
import cProfile

def dec(N,n):   #not used
    while N[n]>N[n+1]:
        if last==0:
            last=9
            dig-=1
        else:
            last-=1
        
def desc(N):   #not used
    for n in range(len(N)-1,-1,-1):
        a=N[n]
        b=N[n-1]
        if N[n-1]>N[n]:
            return n-1
    return len(N)

def recursive(N):   #not used
    bad=desc(N)
    if bad!=len(N):
        N=dec(N,n)
        N=recursive(N)
    return N

def loop(N):
    last=9
    for n in range(len(N)-2,-1,-1):
        cur=int(N[n])
        last=int(N[n+1])
        if cur>last:
            a=N[:n]
            z=N[n+2:]
            while cur>last:
                if last==0:
                    last=9
                    cur-=1
                    z='9'*len(z)
                else:
                    last-=1
            new='%s%s' % (cur,last)
            N=a+str(new)+z
    return N
               
def start():
    file="B-large"                     
    with open(file+'.out', 'wt') as outfile:
        with open(file+".in") as infile:
            T=int(next(infile))
            for t in range(1, T+1):
                line=next(infile).split()
                N=line[0]
                out = int(loop(N))
                casestr="Case #%s: %s\n" % (t,out)
                print(casestr)
                outfile.write(casestr)
                
start()
#print(loop(["---+-++----", 3]))
#cProfile.run("loop([1000000,1000000])")