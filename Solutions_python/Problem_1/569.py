def find_index(q, limit):
    for i in range(q-1,-1,-1):
        if queries[i] not in new_queries[i-limit-1::-1]:
            engine = queries[i]
            index = i
            break
    return engine, index

def find_query(engines, new_queries):
    for engine in engines:
        if engine not in new_queries:
            return True
    return False

cases = []        
n = input()
for i in range(n):
    s = input()
    engines = []
    queries = []
    for j in range(s):
        engines.append(raw_input())
    q = input()
    for j in range(q):
        queries.append(raw_input())
    count = 0
    limit = 0
    new_queries = queries[limit::]
    while not find_query(engines, new_queries):
        engine, limit = find_index(q, limit)
        new_queries = queries[limit::]
        count += 1
    cases.append(count)

for i in range(len(cases)):
    print 'Case #%d: %d' % (i+1,cases[i])
