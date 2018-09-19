#!/usr/bin/env python
import sys

num_cases = -1
num_engines = -1
num_queries = -1

fileIN = open(sys.argv[1], "r")

num_cases = int(fileIN.readline())

for case_num in range(num_cases):
    num_steps = 0
    num_engines = int(fileIN.readline())
    engines = []
    
    for engine_num in range(num_engines):
        engines.append(fileIN.readline().strip())
    
    num_queries = int(fileIN.readline())
    queries = []
    for query_num in range(num_queries):
        queries.append(fileIN.readline().strip())
    
    while queries:
        runs = []
        for engine in engines:
            if not engine in queries:
                runs = [len(queries)]
                break
            runs.append(queries.index(engine))

        for i in range(max(runs)):
            queries.pop(0)
        if queries:
            num_steps += 1

    sys.stdout.write("Case #" + str(case_num+1) + ": " + str(num_steps) + "\n")