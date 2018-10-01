"""
A very simple operation.

"""
import sys
from copy import copy

class TestCase(object):

    def __init__(self, engines, queries):
        self.engines = engines
        self.queries = queries

    def countEnginesUsed(self):
        """
        Presumably if this were in production code for the purpose of prioritizing
        search engines used, we would actually keep track of which search engines
        were being switched to, rather than just how many were used.
        """
        engines_used = 0
        engines_copy = copy(self.engines)
        for query in self.queries:
            if query in engines_copy:
                engines_copy.remove(query)
            if not engines_copy:
                engines_copy = copy(self.engines)
                engines_copy.remove(query)
                engines_used += 1
        return engines_used


def readTestCases(lines):
    test_cases = []
    test_case_count = int(lines[0])
    lines = lines[1:]
    while len(test_cases) < test_case_count:
        engine_count = int(lines[0])
        engines_start = 1
        engines_end = engines_start + engine_count
        engines = lines[engines_start:engines_end]
        query_count = int(lines[engines_end])
        queries_start = engines_end + 1
        queries_end = queries_start + query_count
        queries = lines[queries_start:queries_end]
        test_cases.append(TestCase(engines, queries))
        lines = lines[queries_end:]
    return test_cases 
    

def processInputFile(filepath):
    data = open(filepath, "r").read()
    lines = data.split("\n")
    return readTestCases(lines)

if __name__ == "__main__":
    cases = processInputFile(sys.argv[1])
    case_count = 0
    for case in cases:
        case_count += 1
        print "Case #%d: %s" % (case_count, case.countEnginesUsed())
