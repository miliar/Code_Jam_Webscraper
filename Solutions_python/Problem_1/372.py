import sys
sys.setrecursionlimit(999999999)

def my_find(list, val):
    try:
        return list.index(val)
    except ValueError:
        return -1

def calc_switches(engines, queries, curr_engine=None):
    #print curr_engine
    if curr_engine is not None and queries[0] != curr_engine:
        return calc_switches(engines, queries[1:], curr_engine)

    if any((engine not in queries for engine in engines)):
        return 0

    earliests = [my_find(queries,engine) for engine in engines]
    maxists = max(earliests)
    greatestI = earliests.index(maxists)
    return calc_switches(engines, queries[earliests[greatestI]:], engines[greatestI])+1

def main():
    if len(sys.argv) != 2:
        print "Usage: %s input_file" % sys.argv[0]
        return 1
    
    input_file = open(sys.argv[1])
    num_cases = int(input_file.readline())
    
    for case in xrange(num_cases):
        num_engines = int(input_file.readline())
        engines = []
        for i in xrange(num_engines):
            engines.append(input_file.readline().strip())

        num_queries = int(input_file.readline())
        queries = []
        for i in xrange(num_queries):
            queries.append(input_file.readline().strip())

        switches = calc_switches(engines, queries)

        print "Case #%i: %i" % (case+1, switches)

if __name__ == "__main__":
    sys.exit(main())
