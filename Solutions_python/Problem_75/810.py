#!/usr/bin/python2.6.6

from collections import deque
from os.path import basename
import sys

problem = basename(sys.argv[0]).split('.')[0]
infile = file('in/' + '-'.join((problem, sys.argv[1])) + '.in')
outfile = file('out/' + '-'.join((problem, sys.argv[1])) + '.out', 'w')

cases = xrange(int(infile.readline().strip()))
for case in cases:
    line = deque(infile.readline().strip().split())

    combine = {}
    n = xrange(int(line.popleft()))
    for i in n:
        formula = line.popleft()
        combine[formula[:2]] = formula[2]

    destroy = []
    n = xrange(int(line.popleft()))
    for i in n:
        formula = line.popleft()
        destroy.append(formula)

    line.rotate()
    stack = deque()
    for element in line.popleft():
        stack.append(element)
        latest = ''.join(stack)[-2:]
        if latest in combine:
            stack.pop(); stack.pop()
            stack.append(combine[latest])
        elif latest[::-1] in combine:
            stack.pop(); stack.pop()
            stack.append(combine[latest[::-1]])
        else:
            for d in destroy:
                if d[0] in stack and d[1] in stack:
                    stack.clear()

    result = 'Case #%d: [%s]' % (case+1, ', '.join(stack))
    print result
    outfile.write(result + "\n")

infile.close()
if outfile is not None:
    outfile.close()
