fin=open("input.in","r")
T=(int)(fin.readline())

def gcd(p, q):
    if (q==0): return p
    return gcd(q, p%q)

for t in range(T):
    line=fin.readline().split(' ')
    N=(int)(line[0])
    a=map(int, line[1:])
    a.sort()
    d=a[1]-a[0]
    for i in range(2,N,1): d=gcd(d,a[i]-a[i-1])
    if (a[0]%d==0): y=0
    else: y=d-(a[0]%d)
    print "Case #%d: %d" % (t+1, y)
