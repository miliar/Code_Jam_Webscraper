def rrr(a,b):
    if b==0:
        return a
    if a%b == 0:
        return b;
    else:
        return rrr(b, a%b)


import sys
rl = sys.stdin.readline

cases = int(rl())
for cc in xrange(cases):
    line = map(int, rl().split())
    n = line[0]

    num = []
    for i in range(1, n+1):
        t = line[i]
        num.append(t)
    num.sort(reverse=True)

    terms = []
    for i in range(1, n):
        terms.append( (num[i-1]-num[i]) )
        

    term = terms[0]
    for s in terms:
        term = rrr(term, s)
        
    num.sort()

    while num[0] > 0:
        num[0] = num[0] - term

    print "Case #%d: %d" % (cc+1, num[0]*-1)
    
    
    
    

    
