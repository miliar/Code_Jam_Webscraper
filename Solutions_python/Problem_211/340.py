#!/usr/bin/env python

def prod(l):
    accu = 1.
    for p in l:
        accu *= p
    return accu


def solve(n, k ,u, ps):
    ps.sort()
    #print ps
    spent = 0
    mini = ps[0]
    i = 1
    for i in range(1,n):
        if (ps[i] - mini) * i > u:
            #print mini,"||", i, "||",  ps[i:]
            return ((mini + (u / i))** i) *  prod(ps[i:])
        else:
            u -= (ps[i] - mini) * i
            mini = ps[i]
    #print u, "||", n, "||",  mini
    return min(1., (mini + u/n)**n)
        
        

    
if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    l = l[1:]
    for i in range(1,c+1):
        n, k = [ int(j) for j in l[3*i-3].split() ]
        u = float(l[3*i-2].strip())
        ps = [float(j) for j in l[3*i-1].split() ]

        #print
        #print
        #print l[3*i -3].strip()
        #print l[3*i -2].strip()
        #print l[3*i -1].strip()
        #print "-" * 60
        if n == k:
            sol = solve(n,k,u, ps)
            if sol < 1e-6:
                sol = 0.
        else:
            sol = "NOT IMPLEMENTED"
        print "Case #%d: %s" % (i, sol)

