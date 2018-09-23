
#============================================

parallel = False;
#parallel = True;
curProblem = "A";
curAttempt = 0;
curType = "example";
#curType = "practice-small";
#curType = "practice-large";
#curType = "small";
curType = "large";

exampleString = """3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10
""";

def getInput():
    if curType == "example": return exampleString;

    fileName = "%s-"%(curProblem);
    if curType == "large": fileName = "%s-large.in"%(curProblem);
    if curType == "small": fileName = "%s-small-attempt%d.in"%(curProblem,curAttempt);
    if curType == "practice-small": fileName = "%s-small-practice.in"%(curProblem);
    if curType == "practice-large": fileName = "%s-large-practice.in"%(curProblem);

    with open(fileName, "rt") as f:
        buf = f.readlines();

    return "".join(buf);

def iterateProblems(f, inputData):
    from multiprocessing import Pool;

    pool = Pool(1) if parallel == False else Pool();
    if parallel: resList = [ pool.apply_async(solveProblem, [rnd, inp]) for rnd, inp in enumerate(inputData) ];
    else:        resList = [ solveProblem(rnd, inp) for rnd, inp in enumerate(inputData) ];
    for rnd, res in enumerate(resList):
        if parallel: res = res.get();
        st="Case #%d: %s\n"%(rnd+1,res);
        print st[:-1]; f.write(st);
        stdout.flush();

def parseInput(buf):
    buf = buf.split("\n");
    buf = filter(len,buf);

    outBuf = [];
    T = int(buf[0]); buf=buf[1:];
    for _ in xrange(T):
        D, N = map(int, buf[0].split()); buf=buf[1:];
        arr = [];
        for _ in xrange(N):
            K, S = map(int, buf[0].split()); buf=buf[1:];
            arr.append([K,S]);
        outBuf.append([D, N, arr]);
    return outBuf;

def solveProblem(rnd, x):
    ## Do actions
    
    D, N, arr = x;
    return min( 1.0*D*S/(D-K) for K, S in arr );

#============================================

from time import time;
from sys import stdout;

if __name__ == '__main__':
    inputData = parseInput(getInput());
    outfile = "%s.out"%(curProblem);

    start=time();
    with open(outfile,"wt") as f: iterateProblems(f, inputData);
    print "Total time: %fs"%(time()-start);

#============================================
