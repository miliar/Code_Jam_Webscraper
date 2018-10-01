def analyzeCase(E,Q):
    #~ print E,Q
    unusedE = E[:]
    i=0
    switches = []
    for i,q in enumerate(Q):
        if len(unusedE) == 1 and unusedE[0] == q:
            switches.append((i, unusedE[0]))
            unusedE = E[:]
        try:
            unusedE.remove(q)
        except ValueError:
            # not there, that's okay, just a repeat of an earlier baddie
            pass
    assert len(unusedE)>0

    switches.append((i, unusedE[0]))
    #~ print switches

    return len(switches)-1

if __name__=='__main__':
    xxx = open('test.in').readlines()

    #~ print xxx
    cases = int(xxx.pop(0))
    #~ print cases

    for i in range(cases):
        #~ print "case",i
        engines = int(xxx.pop(0))
        #~ print engines
        E = []
        for j in range(engines):
            #~ print "engine",j
            E.append(xxx.pop(0).strip())
        queries = int(xxx.pop(0))
        Q = []
        for j in range(queries):
            #~ print "engine",j
            Q.append(xxx.pop(0).strip())
        #~ print E,Q
        num = analyzeCase(E,Q)
        print "Case #%d: %d"%(i+1, num)

