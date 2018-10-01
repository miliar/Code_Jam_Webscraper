#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$08.05.2010 6:26:49$"

import sys, fractions

def case(N,q):
    q=list(set(q)) # remove dublications
    N=len(q)
    q.append(q[0]) # cycle for diff
    d=[0]*N
    for i in range(N):
        d[i]=abs(q[i]-q[i+1])
    dm = min(d);
    for i in d:
        dm = fractions.gcd(dm,i)
    if (dm==1): 
        print("STOP: %d,%s => %s,%d" % (N,q,d,dm))
        return 0
    qm=min(q)
    ret=0 if qm%dm==0 else dm-q[0]%dm
    #print("LINE: %d,%s => %s,%d,%d => %s" % (N,q,d,dm,ret,[q[i]+ret for i in range(N)]))
    return(ret)

def direct(N,q,c):
    dmax=1
    for t in range(c*3):
        n=[q[i]+t for i in range(N)]
        d=min(n)
        for i in n:
            d = fractions.gcd(d,i)
        if d>dmax:
            print('Found %d with delta %d' % (d,t))
            dmax=d


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for i in range(T):
                print("Case #%s" % (i+1))
                q=[int(i) for i in infile.readline().rstrip().split()]
                N,q=q[0],q[1:]
                c = case(N,q)
                outfile.write("Case #%s: %d\n" % (i+1,c))
                #direct(N,q,c)

if __name__ == '__main__':
    main()
