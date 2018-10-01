import math

nt = int(raw_input())

for i_it in xrange(nt):
    n,p = map(int,raw_input().split())
    r = map(int,raw_input().split())
    q = []
    for i in xrange(n):
        q.append(map(int,raw_input().split()))
        q[i].sort()
        
    idx = [0]*n
    ans = 0
    while True:
        mrn,mrd = None, None
        exc_idx = None
        ll = None
        lr = None
        #print "Iteration"
        #print idx
        
        for i in xrange(n):
            qi = q[i][idx[i]]
            ri = r[i]
            
            if mrn == None or mrd*qi < mrn*ri:
                mrn = qi
                mrd = ri
                exc_idx = i
            
            
            lli = math.ceil(qi/(1.1*ri))
            lri = math.floor(qi/(0.9*ri))
            #print "i = ", i, " lli = ", lli, " lri = ", lri
            
            ll = lli if ll == None else max(ll,lli)
            lr = lri if lr == None else min(lr,lri)
        
        #print "lr = ",lr, " ll = ", ll
        
        if lr >= ll:
            ans += 1
            for i in xrange(n):
                idx[i] += 1
                
        else:
            idx[exc_idx] += 1
        
        ex = False
        for i in xrange(n):
            if idx[i] >= p:
                ex = True
                break
        if ex:
            break
    
    print "Case #{}: {}".format(i_it+1,ans)
    