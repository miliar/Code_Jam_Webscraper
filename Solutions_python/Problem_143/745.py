import operator
from collections import defaultdict
from test.test_decorators import memoize
num = 0
def solve(instance):
    A, B, K = instance
    result = 0
    print A, B, K
    for a in xrange(A):
        for b in xrange(B):
            if a & b < K:
                result += 1
    return result

def read_input():
#     lines = list(open('B-large-practice.in'))
    lines = list(open('b_ex.in'))
    lines = list(open('B-small-attempt0.in'))
    num_examples = int(lines[0])
    instances = []
    start = True
    count = 0
    for line in map(str.strip, lines[1:]):
        instances.append(map(int, line.strip().split()))
    f = open('output.txt', 'w')
    solns = []
    for case, sol in enumerate(map(solve, instances), 1):
        soln = "Case #%(case)s: %(sol)s" % vars()
        print soln
        solns.append(soln)
    f.write('\n'.join(solns))
read_input()
