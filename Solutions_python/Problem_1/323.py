def calc_num_switches(engines,queries):
    switches = dict([(e,0) for e in engines])
    queries.reverse()
    for q in queries:
        possible_switches = [switches[x] for x in engines if x != q]
        switches[q] = min(possible_switches) + 1
    
    possible_switches = [switches[x] for x in engines]
    return min(possible_switches)

import sys

lines = file(sys.argv[1]).readlines()
cases_count = int(lines[0])
current_line = 1
for case_count in range(1,cases_count+1):
    
    # Read engines
    
    engines_count = int(lines[current_line].strip())
    current_line += 1
    engines = []
    for engine_id in range(current_line,current_line+engines_count):
        engines.append(lines[engine_id].strip())

    current_line += engines_count

    #Read queries

    queries_count = int(lines[current_line].strip())
    current_line += 1
    queries = []
    for query_id in range(current_line,current_line+queries_count):
        queries.append(lines[query_id].strip())
    current_line += queries_count

    solution = calc_num_switches(engines,queries)
    print "Case #%d: %s" % (case_count, solution)

if current_line != len(lines):
    print "BAD!!!!!!!!!!!!!!!!!!!!! MISSED A CASE!!!!!!!!!!!"
