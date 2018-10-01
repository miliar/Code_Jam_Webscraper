def f(n,k):
    x,y,cx,cy = n-1,n,0,1
    while k > (cx+cy):
        k -= cx+cy
        if x & 1: # (2k-1,2k) -> (k-1,k)
            x,y,cx,cy = x/2,y/2,cx,cx+2*cy
        else: #(2k,2k+1)->(k,k+1)
            x,y,cx,cy = x/2,(y+1)/2,2*cx+cy,cy
    if k > cy:
        return (x/2-1,(x+1)/2-1)
    else:
        return (y/2-1,(y+1)/2-1)

def g(n,k):
    pool = [n-1]
    x = y = None
    for _ in range(k):
        n = max(pool)
        x,y = (n-1)/2, n/2
        pool.remove(n)
        pool.extend([x,y])
        #print n,'->',(x,y)
    return (y,x)

t = input()
for icase in range(1,t+1):
    n,k = map(int,raw_input().split())
    x,y = sorted(f(n+1,k))
    print 'Case #%d: %d %d' % (icase, y, x)
