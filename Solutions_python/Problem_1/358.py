#!/usr/bin/env python
"""
Saving The Universe
"""
import sys

def do_case(search_engines, queries):
    num_switches = 0
    total_distance = 0

    if not len(queries):
        return 0

    while total_distance < len(queries):
        max_distance = 0
        max_engine = None

        for engine in search_engines:
            for counter, query in enumerate(queries[total_distance:]):
                if query == engine:
                    if counter > max_distance:
                        max_distance = counter
                        max_engine = engine
                    break
                elif counter + 1 == len(queries[total_distance:]):
                    max_distance = counter + 1
                    max_engine = engine
        num_switches += 1
        total_distance += max_distance

    return num_switches - 1

def main(lines):
    num_cases = int(lines[0])
    lines = lines[1:]

    for case in xrange(1, num_cases + 1):
        start_offset = 0

        # Get search engines.
        num_search_engines = int(lines[0])
        search_engines = lines[start_offset + 1:num_search_engines + 1]
        start_offset += num_search_engines + 1

        # Get queries.
        num_queries = int(lines[start_offset])
        queries = lines[start_offset + 1:num_queries + start_offset + 1]
        start_offset += num_queries + 1

        # Calculate case and display results.
        num_switches = do_case(search_engines, queries)
        print 'Case #%d: %d' % (case, num_switches)

        lines = lines[start_offset:]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: %s <input>' % (sys.argv[0])
        raise SystemExit
    try:
        main(open(sys.argv[1], 'r').read().splitlines())
    except IOError, e:
        print 'Fatal error:', e
