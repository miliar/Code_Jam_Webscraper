#!/usr/bin/env python

def get_frequency_list(engines, queries):
    options = list(engines)
    result = []
    counter = 0
    for query in queries:
        if not query in options:
            continue
        if len(options) == 1 and options[0] == query:
            counter += 1
            result.append(query)
            options = list(engines)
            options.remove(query)
        else:
            options.remove(query)
    return counter

if __name__ == "__main__":
    n_cases = int(raw_input())
    for i_case in range(n_cases):
        search_engines = []
        queries = []
        n_search_engines = int(raw_input())
        for i_search_engines in range(n_search_engines):
            search_engines.append(raw_input())
        n_queries = int(raw_input())
        if not n_queries:
            print "Case #%d: 0" % (i_case + 1)
            continue
        for i_query in range(n_queries):
            queries.append(raw_input())
        n_switches = \
            get_frequency_list(search_engines, queries)
        print ("Case #%d: %d"
               % (i_case + 1, n_switches))
