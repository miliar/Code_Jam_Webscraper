#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Python for Google Code Jam 2008 Round 1

Minimum Scalar Product
'''

def solve_problems(inputs):
    r'''Generate output for the problem

    Example:
    >>> input = """\
    ... 2
    ... 3
    ... 1 3 -5
    ... -2 4 1
    ... 5
    ... 1 2 3 4 5
    ... 1 0 1 0 1
    ... """
    >>> print solve_problems(input)
    Case #1: -25
    Case #2: 6
    <BLANKLINE>
    '''
    line = inputs.split("\n")
    l = 0

    num_cases = int(line[l])
    l+=1
    solution = []

    for c in xrange(num_cases):
        # parse out bits
        size = int(line[l])
        l+=1

        v1 = [int(x) for x in line[l].split()]
        l+=1
        v2 = [int(x) for x in line[l].split()]
        l+=1
        assert(len(v1) == len(v2))
        assert(len(v1) == size)
        solution.append(solve(v1, v2))

    output = []
    for s, n in zip(solution, xrange(1, num_cases+1)):
        output.append("Case #%d: %d"%(n, s))
    return "\n".join(output) + "\n"

def solve(vec1, vec2):
    '''Solve a problem instance

    Example:
    >>> v1 = [1,3,-5]
    >>> v2 = [-2,4,1]
    >>> print solve(v1, v2)
    -25
    '''
    m = 10**10
    p1s = all_perms(vec1)
    p2s = all_perms(vec2)
    for p1 in p1s:
        for p2 in p2s:
          sum = add(p1, p2)
          #print p1, p2, sum, m
          if sum < m: m = sum
    return m

def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def add(vec1, vec2):
    sum = 0
    for x, y in zip(vec1, vec2): sum += x*y
    return sum

def _usage():
    print "Usage: %s <input_file> <output_file>"%sys.argv[0]
    print "If output_file omitted, printed to stdout"

def _test():
    import doctest
    return doctest.testmod()

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        _usage()
        print "Running test suite..."
        failed, total = _test()
        if (not failed): print "All %d tests passed"%total
    elif len(sys.argv) == 2:
        inputs = file(sys.argv[1]).read()
        print solve_problems(inputs)
    elif len(sys.argv) == 3:
        inputs = file(sys.argv[1]).read()
        file(sys.argv[2],"w").write(solve_problems(inputs))
    else:
        _usage()
        sys.exit(1)
