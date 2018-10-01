for case in range(int(raw_input())):
    p, q = [int(i) for i in raw_input().split('/')]
    
    a = ''
    if q % p == 0:
        q = q/p
        p = 1
    t = q
    while t % 2 != 1:
        t = t/2
    if t != 1 or p > q:
        a = 'impossible'
    else:        
        k = 0
        while q != 1 and p < q:
            q = q/2
            k += 1            
        if k == 0:
            a = 'impossible'
        else:
            a = str(k)

    print "Case #" + str(case + 1) + ": " + a
    