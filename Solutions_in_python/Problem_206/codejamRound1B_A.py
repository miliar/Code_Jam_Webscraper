t=input()
for i in range(t):
    d,n=map(int,raw_input().split())
    k,s=map(int,raw_input().split())
    v=float(d)*s/(d-k)
    for j in range(n-1):
        k1,s1=map(int,raw_input().split())
        v1=float(d)*s1/(d-k1)
        if v1<=v:
            v=v1
    print "Case #%d: %f" %(i+1,v)
