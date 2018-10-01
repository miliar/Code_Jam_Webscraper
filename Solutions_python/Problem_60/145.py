import sys
f = open(sys.argv[1])
cases = int(f.readline())

def nums(f):
    return [int(x) for x in f.readline().split()] 

class Chicken:

    def __init__(self, x, v, cando, push):
        self.x = x # starting pos
        self.p = x # current pos
        self.v = v # velocity
        self.cando = cando # can finish (with swaps)
        self.push = push # chosen finisher

    def __repr__(self):
        s = self
        return "(%d,%d,%d,%d,%d)" % (s.x,s.p,s.v,int(s.cando),int(s.push))

def log(fmt, *args):
    if 0:
        print fmt % args

for case in range(1,cases+1):
    N, K, B, T = nums(f)
    X = nums(f)
    V = nums(f)
    log("%d, %d, %d, %d, %s, %s", N, K, B, T, X, V)
    can = [ x+T*v>=B for x,v in zip(X,V) ]
    log("%s, %d", can, sum(can))

    # do we have K chickens that can make it
    if sum(can) < K:
        print "Case #%d: IMPOSSIBLE" % case
        continue

    # select rightmost K chickens that can make it for pushing
    i = len(X)-1
    k = 0
    push = [False] * N
    while k < K:
        if can[i]:
            push[i] = True
            k = k+1
        i = i-1
    log("%s", push)
    C = [Chicken(x,v,_can,_push) for x,v,_can,_push in zip(X,V,can,push)]
    log("%s", C)

    t = 0
    swaps = 0
    while t < T:
        # Advance the chickens according to the rules
        for i in xrange(N-1,-1,-1):
            newp = C[i].p + C[i].v
            j = i
            while j < N-1 and newp > C[j+1].p:
                if C[j].push and not C[j+1].push:
                    swaps += 1
                    C[j], C[j+1] = C[j+1], C[j]
                    j = j+1
                else:
                    newp = C[j+1].p
            C[j].p = newp
        t += 1
        log(str(C))
    print "Case #%d: %d" % (case, swaps)

