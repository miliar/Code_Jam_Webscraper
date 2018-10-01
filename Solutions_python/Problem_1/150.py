case_number = 1
N = int(raw_input())
for i in xrange(N):
    
    switches = 0
    S = int(raw_input())
    engines = []
    for i in xrange(S):
        engines.append(raw_input())
    
        
    Q = int(raw_input())
    queries = []
    
    for i in xrange(Q):
        queries.append(raw_input())
    
    while True:
        best_next_match = -1
        for engine in engines:
            try:
                next_match = queries.index(engine)
            except ValueError:
                next_match = len(queries)
            
            if (next_match > best_next_match):
                best_next_match = next_match
        
        queries = queries[best_next_match:]
        if len(queries) == 0:
            break
        switches += 1
    
    print "Case #%d: %d" % (case_number, switches)
    case_number += 1
    