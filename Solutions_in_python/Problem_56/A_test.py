#! /usr/bin/python

#  (c) 2010 Wott (http://wott.net.ru/ , wott@gmail.com)

__author__="Wott"
__date__ ="$22.05.2010 5:09:26$"

import sys

def case(N,K,m):
    n=['.'*N+i.replace('.','') for i in m] # rotate and gravity
    nf=[''.join([s[-1-i] for s in n]) for i in range(N)] # flip
    nw=['.'*N]*N+n+['.'*N]*N # envelop with empty
    d1=[''.join([nw[N+i+j][-1-i] for i in range(N)]) for j in range(-N+1,N)]    #down
    d2=[''.join([nw[N-i+j][-1-i] for i in range(N)]) for j in range(2*N)]       #up
    nl='.'.join(n+nf+d1+d2) # linear all
    b=r=0 # find winner
    if -1!=nl.find('B'*K): b=1
    if -1!=nl.find('R'*K): r=1
    # print ("Blue: %d, Red %d" % (b,r))
    ret=['Neither','Red','Blue','Both'][b*2+r]
    #print("LINE: %d,%d,%s => %s" % (N,K,m,ret))
    print("LINE: %d,%d => %s" % (N,K,ret))
    return(ret)

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: %s in.file out.file" % sys.argv[0])
        return
    with open(args[0]) as infile:
        with open(args[1],'w') as outfile:
            T = int(infile.readline())
            for t in range(T):
                N,K=[int(i) for i in infile.readline().rstrip().split()]
                m=[]
                for i in range(N):
                    m.append(infile.readline().rstrip());
                c = case(N,K,m)
                outfile.write("Case #%s: %s\n" % (t+1,c))

if __name__ == '__main__':
    main()
