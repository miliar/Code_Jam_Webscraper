def process(es, qs):
    S = len(es)
    Q = len(qs)
    if Q==0:
        return 0
    prow = list(0 for i in range(S))
    row = list()
    for q in qs :
        row = list()
        for e in range(S):
            if q == es[e]:
                row.append(1000000)
            else:
                row.append(min(prow[e], min(prow) + 1))
        prow = row
    return min(row)


def universe(filename):
    fin = open(filename+'.in','r')
    fout = open(filename+'.out','w')
    
    N = int(fin.readline())

    for case in range(N):
        S = int(fin.readline())
        engines = []
        for s in range(S):
            engines.append(fin.readline())
        Q = int(fin.readline())
        queries = []
        for q in range(Q):
            queries.append(fin.readline())
        
        result = process(engines, queries);
        print >>fout, 'Case #%d: %s' % (case+1, result)
    fout.close()
    fin.close()

universe('A-large')

