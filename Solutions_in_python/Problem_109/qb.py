
#============================================

def readBuffer():
    #'''
    with open(infile,"rt") as f: buf = f.readlines();
    buf=map(lambda x: x[:-1], buf);
    '''
    buf = """2
2 6 6
1 1
3 320 2
4 3 2
    """.split("\n");
    #'''

    t = int(buf[0]); buf=buf[1:];
    buf2 = [];
    for _ in xrange(1,t+1):
        n,w,l = parse(buf[0],"iii"); buf=buf[1:];
        arr = parse1(buf[0],"I0",[n]); buf=buf[1:];
    
        buf2.append([n, w, l, arr]);
        pass;
    return buf2;

def initQueue(q):
    solveProblem.q = q;

def solveProblem((rnd,(n,w,l,arr))):
    ## Do actions
    
    ind=1;
    while True:
        print "Attempt #%d"%ind;
        ind += 1;
        
        p=[];
        for i in xrange(n): p.append([w*random(), l*random()]);

        for i in xrange(n):
            x0,y0 = p[i];
            r0 = arr[i];
            for j in xrange(i+1,n):
                x1,y1 = p[j];
                r1 = arr[j];
                if(hypot(x1-x0,y1-y0) < r0+r1): break;
            else: continue;
            break;
        else: break;

    i = solveProblem.q.get();
    print "%d >> Done, %s left\n"%(rnd+1,i);
    sys.stdout.flush();
    return p;

#============================================

from argparser import parse, parse1;
from multiprocessing import Pool, Queue;
from random import random;
from time import time;
from math import hypot;
import sys;

if __name__ == '__main__':
    infile = "B-small-attempt0.in";
    #infile = "B-large.in";
    outfile = "B.out";

    buf=readBuffer();
    start=time();
    with open(outfile,"wt") as f:
        q = Queue();
        for i in xrange(len(buf)-1,-1,-1): q.put(i);

        if(False):
            p = Pool(None, initQueue, [q]);
            res = p.map(solveProblem,enumerate(buf));
        else:
            initQueue(q);
            res = map(solveProblem,enumerate(buf));

        for rnd,r in enumerate(res):
            st="Case #%d: %s\n"%(rnd+1," ".join(map(lambda x: "%f %f"%(x[0],x[1]), r)));
            print st[:-1]; f.write(st);

    print "Total time: %fs"%(time()-start);

#============================================
