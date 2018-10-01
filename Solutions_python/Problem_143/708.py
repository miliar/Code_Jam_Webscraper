def f(m,n,k):
    count = 0
    for i in xrange(m):
        for j in xrange(n):
            if i&j<k:
                    count+=1
    return count

t = input()
for i in xrange(t):
    m,n,k = map(int,raw_input().split())
    print "Case #"+str(i+1)+":",f(m,n,k)
    
