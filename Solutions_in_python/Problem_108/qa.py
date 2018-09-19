
#============================================

def readBuffer():
    #'''
    with open(infile,"rt") as f: buf = f.readlines();
    buf=map(lambda x: x[:-1], buf);
    '''
    buf = """4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14
    """.split("\n");
    #'''

    t = int(buf[0]); buf=buf[1:];
    buf2 = [];
    for _ in xrange(1,t+1):
        n = parse1(buf[0], "i"); buf=buf[1:];
        arr = [parse(buf[i],"ii") for i in xrange(n)]; buf=buf[n:];
        d = parse1(buf[0], "i"); buf=buf[1:];
    
        buf2.append([d, arr]);
        pass;
    return buf2;

def initQueue(q):
    solveProblem.q = q;

def rec(dist,arr,r,ind):
    d,_ = arr[ind];
    key=(r,ind);
    if(key in db): return False;
    if(d+r >= dist): return True;

    #print "d=%s, r=%s"%(d,r);

    for ind2 in xrange(ind+1,len(arr)):
        d2,r2 = arr[ind2];
        if(d2 > d+r): continue;
        r2 = min(r2,d2-d);
        
        #print "[%d] d2=%s, r2=%s"%(ind2,d2,r2);
        
        if(rec(dist,arr,r2,ind2)): return True;
    
    db.add(key);
    return False;

def solveProblem((rnd,(d,arr))):
    global db;
    ## Do actions
    print "d=%s, arr=%s"%(d,arr);
    db=set([]);
    ret = rec(d,arr,arr[0][0],0);

    i = solveProblem.q.get();
    print "%d >> Done, %s left\n"%(rnd+1,i);
    sys.stdout.flush();
    return ret;

#============================================

from argparser import parse, parse1;
from multiprocessing import Pool, Queue;
from time import time;
import sys;

if __name__ == '__main__':
    infile = "A-small-attempt0.in";
    #infile = "A-large.in";
    outfile = "A.out";

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
            st="Case #%d: %s\n"%(rnd+1,"YES" if r else "NO");
            print st[:-1]; f.write(st);

    print "Total time: %fs"%(time()-start);

#============================================
