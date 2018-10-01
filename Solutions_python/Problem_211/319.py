
            

def prob (n, k, u, p):
    #print p
    m = (sum(p) + u) / n
    #print m
    p1 = []
    ans = 1
    for i in range(n):
        if p[i] <= m:
            p1.append(p[i])
        else:
            ans *= p[i]
    #print "p1: %s" % str(p1)
    if len(p1) == len(p) or len(p1) == 0:
        return m**n
    else:
        return ans*prob(len(p1), k, u, p1)
    
t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input()
    (n, k) = map(lambda x: int(x), line.split(' '))
    line = raw_input()
    u = float(line)
    line = raw_input()
    p = map(lambda x: float(x), line.split(' '))
    print "Case #{}: {}".format(i, prob(n, k, u, p))
