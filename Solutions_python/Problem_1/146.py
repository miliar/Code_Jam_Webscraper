import sys

def cmp_by_count(x, y):
    return x['count'] - y['count']

def input_case():
    case = {}
    
    case['engines'] = {}
    num_engines = int(f.readline())
    for i in xrange(int(num_engines)):
        case['engines'][f.readline().strip()] = { 'count' : 0 }
    
    case['queries'] = []
    num_queries = int(f.readline())
    for i in xrange(int(num_queries)):
        q = f.readline().strip()
        case['queries'].append(q)
        case['engines'][q]['count'] += 1
    return case

def solve_case(case):
    candidates = [{ 'engine' : k, 'count' : case['engines'][k]['count'] } for k in case['engines']]
    candidates.sort(cmp_by_count)
        
    iqueries = 0
    num_switches = 0
    while iqueries < len(case['queries']):
        distances = [get_distance(candidate['engine'], case['queries'][iqueries:]) for candidate in candidates]
        distances.sort()
        
        if distances[0] == -1:
            break
        else:
            iqueries += distances[-1]
            num_switches += 1
    
    return num_switches

def get_distance(engine, queries):
    try: 
        distance = queries.index(engine)
    except ValueError:
        distance = -1
    return distance

f = open(sys.argv[-1], 'r')
num_cases = int(f.readline())

for i in xrange(int(num_cases)):
    case = input_case()
    print 'Case #' + str(i + 1) + ': ' + str(solve_case(case)) #format it correctly, dummy

f.close()