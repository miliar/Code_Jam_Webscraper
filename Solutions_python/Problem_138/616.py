def fn():
    n = int(raw_input())
    g = map(float,raw_input().split())
    b = map(float,raw_input().split())
    
    b.sort()
    g.sort()
    
    i = 0
    j = 0
    a1 = 0
    
    while(j<n):
        if (b[j]>g[i]):
            i+=1
            j+=1
            a1+=1
        else:
            j+=1
            
    i=0
    j=0
            
    a2=0
    
    while(i<n):
        if (b[j]<g[i]):
            i+=1
            j+=1
            a2+=1
        else:
            i+=1

    return str(a2)+" "+str(n-a1)
t = int(raw_input())

for i in range(t):
    print "Case #"+str(i+1)+": "+str(fn())

