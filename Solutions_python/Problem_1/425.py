import sys

def first_indices(engines, queries):
    return dict([(e, queries.index(e)) for e in engines if e in queries])

def missing_engines(engines, indices):
    return [e for e in engines if not e in indices]

def process_queries(case_number, engines, queries, path=None):
    root = False

    if path is None:
        #print "\n\n\nCase #%d" % case_number
        #print "creating path"
        root = True
        path = []

    indices = first_indices(engines, queries)

    if len(indices) < len(engines):
        if root:
            print "Case #%d: 0" % case_number
        else:
            path.append(missing_engines(engines, indices)[0])
            #print "returning path: %s" % path
        return

    i = max(indices.values())
    path.append(queries[i])
    process_queries(case_number, engines, queries[i:], path)

    if root:
        print "Case #%d: %d" % (case_number, len(path)-1)
        #print "Path: %s" % path

def main():
    f = sys.stdin
    test_cases_n = int(f.readline())
    line = 2

    for i in xrange(test_cases_n):

#        print "test case #%d starts in line %d" % (i+1, line)

        engines = []
        queries = []

        search_engines_n = int(f.readline())
        line += 1
        for s in xrange(search_engines_n):
            engines.append(f.readline().strip())
            line += 1
        queries_n = int(f.readline())
        line += 1
        for q in xrange(queries_n):
            queries.append(f.readline().strip())
            line += 1

        process_queries(i+1, engines, queries)

if __name__ == '__main__':
    main()
