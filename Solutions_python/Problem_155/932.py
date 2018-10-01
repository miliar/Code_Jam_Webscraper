t=input()
for _ in range(t):
    (m,r)=raw_input().strip().split()
    m=int(m)
    standing=int(r[0])
    new=0
    for i in range(1,m+1):
        if standing<i:
            new+=i-standing
            standing=i+int(r[i])
        else:
            standing+=int(r[i])
    print 'Case #{}: {}'.format(_+1,new)
