#!/usr/bin/env python

"""
    N: cases
    S: number of search engines
    Q: number of queries
"""
__author__ = "Yoan Blanc <yoan@dosimple.ch>"

import os
import re
import sys

MODE = "debug"

MODES = {
    "small": {
        "in": "A-small.in",
        "out": "A-small.out",
    },
    "large": {
        "in": "A-large.in",
        "out": "A-large.out",
    },
    "debug": {
        "in": "A.in",
        "test": "A.test"
    }
}

def parse_input(filename):
    if isinstance(filename, file):
        fp = filename
    else:
        fp = open(filename, "r")
    
    cases = []
    try:
        N = int(fp.next())
        for case in xrange(N):
            S = int(fp.next())
            search_engines = []
            queries = []
            for search_engine in xrange(S):
                search_engines.append(fp.next()[:-1])
            Q = int(fp.next())
            for query in xrange(Q):
                queries.append(fp.next()[:-1])
            cases.append({
                "search_engines": search_engines,
                "queries": queries
            })
    finally:
        fp.close()

    return cases

def generate_output(filename, results):
    if isinstance(filename, file):
        fp = filename
    else:
        fp = open(filename, "w")

    i = 0
    for result in results:
        i+=1
        fp.write("Case #%d: %s\n" % (i, result))
    fp.close()

def calc_results(cases):
    results = []
    for case in cases:
        counter = 0
        memory = []
        for query in case["queries"]:
            if not query in memory:
                memory.append(query)
                if len(memory) == len(case["search_engines"]):
                    memory = [query]
                    counter += 1
        results.append(str(counter))
    return results

def test(filename, results):
    if isinstance(filename, file):
        fp = filename
    else:
        fp = open(filename, "r")
    
    case = re.compile(r'Case\s#(?P<index>\d+):\s+(?P<result>.+)')
    try:
        for line in fp:
            matches = case.match(line)
            if matches:
                index = int(matches.group("index"))
                assert results[index-1] == matches.group("result"), "Case %d:\n expected:\t%s\n got:\t\t%s" % (index, matches.group("result"), results[index-1])
            else:
                raise Exception, "line fail: %s" % line
    finally:
        fp.close()

def main(argv):
    if len(argv) > 1 and argv[1] in MODES:
        mode = MODES[argv[1]]
    else:
        mode = MODES[MODE]
    
    cases = parse_input(mode["in"])
    results = calc_results(cases)
    if "test" in mode:
        try:
            test(mode["test"], results)
            print "all %s tests are ok" % len(results)
        except AssertionError, e:
            print e
    else:
        generate_output(mode["out"], results)
    return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
