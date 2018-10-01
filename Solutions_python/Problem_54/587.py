def gcd(a,b):
    if a==0:return b
    return gcd(b%a,a)

def lcm(a,b):
    if a==0 and b==0: return 0
    return (a*b)/gcd(a,b)
 
f=open("B-large.in")

n=int(f.readline())

for i in range(n):
    ll=[int(x) for x in (f.readline()).split(" ")[1:]]
    ll.sort()
    g=ll[1]-ll[0]
    for k in range(len(ll)):
        for l in range(k):
            g=gcd(g,ll[k]-ll[l])
    m=1
    for x in ll:
        m=lcm(m,(g-x%g)%g)
    print "Case #"+str(i+1)+": "+str(m)

