import sys
import cStringIO as StringIO

#f = file('/Users/larsr/Downloads/A-small-attempt0.in')
f = file('/Users/larsr/Downloads/A-large.in')
#with sys.stdin as f:

ff= StringIO.StringIO("""\
4
2 20 10
2 10 0
4 25 25 25 25
3 24 30 21
""")


T = int(f.readline())
for case in range(1,T+1):
    print 'Case #%d:' % case,
    vals = [int(x) for x in f.readline().strip().split()]
    N = vals[0]
    P = vals[1:]
    X = float(sum(P))
    for i in range(N):
        fmin=0.0
        fmax=1.0
        while fmax-fmin>(10.**-14):
            frac = (fmax+fmin)/2.
            mine = P[i]+frac*X
            Less = [ P[j] for j in range(N) if j!=i and P[j] < mine ]            
            OthersNeed = sum([mine-x for x in Less])/X
            if OthersNeed+frac >=1.0:
                fmax = frac
            else:
                fmin = frac
        print (round(frac*(10**10)))/float(10**8),
    print
    
    #mine + frac*X == othersneed+sum(less)