INPUT = 'A-large.in'
OUTPUT = INPUT.replace('.in', '.out')

f = open(INPUT, 'r')
input = f.readlines()
f.close()
N = eval(input[0])
input = input[1:]

f = open(OUTPUT, 'w')

def remove_duplicates(l):
    if len(l) == 0:
        return []
    tmp = [l[0]]
    for i in xrange(1, len(l)):
        if tmp[-1] != l[i]:
            tmp.append(l[i])
    return tmp

def do_it_greedy(l, n):
    """l = list of queries, n - number of search engines"""
    count = 0
    t = 0
    while t < len(l):
        tmp = t
        for i in xrange(n):
            try:
                tmp = max(l.index(i, t), tmp)
            except ValueError:
                return count
        t = tmp
        count += 1
    return count
            

case = 0
i = 0
while case < N:
    case += 1
    num_engines = eval(input[i].strip())
    i += 1
    engines = {}
    for j in xrange(num_engines):
        tmp = input[i + j].strip()
        engines[tmp] = j
    i += num_engines
    
    num_queries = eval(input[i].strip())
    i += 1
    queries = []
    for j in xrange(num_queries):
        tmp = input[i + j].strip()
        if engines.has_key(tmp):
            queries.append(engines[tmp])
        else:
            queries.append(tmp)
    queries = remove_duplicates(queries)
    print 'case ', case
    if len(queries) == 0:
        print queries, 0
        f.write('Case #%d: %d\n' % (case, 0))
        continue
    i += num_queries
    num_switches = do_it_greedy(queries, num_engines)
    print queries, num_switches
    f.write('Case #%d: %d\n' % (case, num_switches))
    

f.close()
