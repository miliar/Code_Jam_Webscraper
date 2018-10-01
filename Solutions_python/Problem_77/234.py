"""
QR2011 D
http://code.google.com/codejam/contest/dashboard?c=975485#s=p3
"""

if __name__ == "__main__":
    f = open("D-large.in")
    T = int(f.readline())
    for t in range(T):
        N = int(f.readline())
        L = [ int(x) for x in f.readline().split() ]
        
        groups = []
        G = dict(zip(range(1,N+1), L))
        while(G):
            group = []
            start = G.keys()[0]
            a = start
            while 1:
                group += [a]
                a = G.pop(a)
                if a == start:
                    break
            groups += [group]
        
        num = sum([len(x) for x in groups if len(x) > 1])
        print "Case #%d: %f" % (t+1, num)
