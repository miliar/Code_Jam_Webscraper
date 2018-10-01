n = int(raw_input())

for i in xrange(n):
    
    case = raw_input().strip().split()
    smax = int(case[0])
    slist = case[1]
    sumsofar = 0
    res = 0
    for shyness,si in enumerate(slist):
        nshi = int(si)
        if sumsofar < shyness:
            res += (shyness - sumsofar)
            sumsofar = shyness

        sumsofar += nshi
            
        
        
    print "Case #{0}: {1}".format(i+1, res)