data = open('A-large.in')
num_case = int(data.next())
for i in xrange(num_case):
    """Get data"""
    num_searchEngs = int(data.next())
    searchEngs = []
    for j in xrange(num_searchEngs):
        searchEngs.append(data.next().rstrip())
    num_queries = int(data.next())
    queries = []
    for j in xrange(num_queries):
        query = data.next().rstrip()
        # Ignore neighbouring repeated queries
        if queries != [] and queries[-1] == query:
            pass
        else:
            queries.append(query)
    
    """Do calculation"""
    num_swithes = 0
    hasGotAns = False
    while queries != []:
        for searchEng in searchEngs:
            if searchEng not in queries:
                hasGotAns = True
                break
        if hasGotAns:
            break
        else:
            num_swithes += 1
            pos = max([queries.index(searchEng) for searchEng in searchEngs])
            for j in xrange(pos):
                queries.pop(0)   

    """Print results"""    
    print 'Case #%s: %s' % (i+1, num_swithes)
            
