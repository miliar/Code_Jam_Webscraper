t = int(raw_input())
n = t
while (t) :
    s = raw_input()
    l = s.split(" ")
    c,f,x = float(l[0]),float(l[1]),float(l[2])
    ts = 0.0
    cf = 2.0
    tx = x/cf
    tc = c/cf
    cf = cf+f
    tp = tx
    while(1) :
        ts = ts + tc
        tx = x/cf
        tc = c/cf
        tn = ts + tx
        cf = cf+f
        if (tn<tp) :
            tp = tn
            #print tp
            pass
        else : break
    print ('Case #%d: %f')%(n-t+1,tp)
    t-=1

        
        
        
