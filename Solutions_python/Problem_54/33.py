def gcd(a,b):
    if (a < b):
        aux = b
        b = a
        a = aux
    if b == 0:
        return a
    return gcd(b,a%b)
        

ntest = int(raw_input())

for case in xrange(ntest):
    print "Case #" + str(case+1) + ": ",
    ent = map(int,raw_input().split(' '))
    n = ent[0]
    l = ent[1:]
    l.sort()
    b = []
    for i in xrange(len(l)-1):
        b.append(l[i+1]-l[i])
    
    g = b[0]
    for e in b:
        g = gcd(g,e)

    maxv = l[-1]
    next = ((maxv+g-1)/g)*g
    #print g, maxv, next
    print next - maxv
                   
