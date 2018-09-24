num_cases = int(raw_input())

for case_count in range(0, num_cases):
    num_engines = int(raw_input())

    list_queries = []

    for engine_count in range(0, num_engines):
        engine = raw_input()
    
    num_queries = int(raw_input())

    for queries_count in range(0, num_queries):
        query = raw_input()
        list_queries.append(query)


    # resolver o problema
    num_switches = 0
    hash_queries = {}
    query_count = 0
    
    for query in list_queries:
        if not hash_queries.has_key(query):
            hash_queries[query] = 1 # marcar
            if query_count < engine_count:
                query_count += 1
            elif query_count == engine_count:
                query_count = 1
                num_switches += 1
                hash_queries.clear()
                hash_queries[query] = 1

    print '%(case)s%(case_num)d%(ch)s %(switches)d' % {'case': "Case #", 'case_num':(case_count+1), 'ch':":", 'switches':num_switches}
