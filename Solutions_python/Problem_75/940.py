import sys
import itertools

class Runner(object):
    def __init__(self, test_case):
        self.test_case = test_case
    def run(self):
        self.element_list = []
        def try_combinations():
            def last_two():
                try:     return str(sorted(self.element_list[-2:]))
                except:  return None
            combo = last_two()
            if not combo: return
            if combo in self.test_case.combinations:
                replacement = self.test_case.combination_lookup[combo]
                self.element_list.pop(); self.element_list.pop()
                self.element_list.append(replacement)

        def try_oppositions():
            def all_combinations():
                return itertools.combinations(set(self.element_list), 2)
            for combo in all_combinations():
                if combo in self.test_case.oppositions:
                    self.element_list = []
                    return

        for invocation in self.test_case.invocations:
            self.element_list.append(invocation)
            try_combinations()
            try_oppositions()

        final_element_list = "[" + ", ".join(self.element_list) + "]"
        print 'Case #%d: %s' % (self.test_case.number, final_element_list)

class TestCase(object):

    def build_combinations(self, l):
        self.combinations = set()
        self.combination_lookup = {}
        if not l:
            return
        for spec in l:
            # sort combo for quick set lookup (half size), stringify for hashable lookup.
            left, right, replacement = spec
            combo = str(sorted((left, right)))
            self.combinations.add(combo)
            self.combination_lookup[combo] = replacement

    def build_oppositions(self, l):
        self.oppositions = set()
        if not l:
            return
        for spec in l:
            # add both directions for quicker lookup.
            left, right = spec
            self.oppositions.add((left, right))
            self.oppositions.add((right, left))

    def __init__(self, spec_string, number):
        self.number = number
        self.oppose  = []
        self.invocations = []
        spec = spec_string.strip().split(" ")

        c = int(spec[0])
        self.build_combinations(spec[1:c+1])

        d = int(spec[c+1])
        self.build_oppositions(spec[c+2:c+2+d])

        self.invocations = list(spec[c+2+d+1])

        # print "COMBINATIONS:", self.combinations
        # print "COMBINATION LOOKUPS:", self.combination_lookup
        # print "OPPOSITIONS:", self.oppositions
        # print "INVOCATIONS:", self.invocations
        # print


def read_input():
    lines = sys.stdin.readlines()
    return [TestCase(test_case_spec, test_case_number) for test_case_spec, test_case_number in zip(lines[1:], xrange(1, len(lines))) ]

if __name__ == '__main__':
    test_cases = read_input()
    for test_case in test_cases:
        Runner(test_case).run()
