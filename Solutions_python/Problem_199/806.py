import math

nt = int(input())
for it in xrange(nt):
    r,k = raw_input().split()
    k = int(k)
    n = len(r)
    
    aux = [0]*n
    resp = 0; op = 0;    
    for i in xrange(n):
        op += aux[i]
        cur = (1 if r[i] == '+' else 0) + op
        cur %= 2
        if cur == 0:            
            ri = i+k-1
            if ri > n-1:
                resp = -1
                break
            resp += 1
            op += 1
            if ri+1 < n: aux[ri+1] -= 1
            

    print "Case #{}: {}".format(it+1, resp if resp >= 0 else "IMPOSSIBLE")