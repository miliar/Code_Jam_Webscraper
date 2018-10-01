INPUT = """
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
"""

OUTPUT = """
Case #1: 6
Case #2: 100
Case #3: 4
"""

import os, itertools

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)




def solve(line):
    tokens = iter(line.split(' '))

    n_combine = int(next(tokens))
    combine = {}
    for n in range(n_combine):
        rule = next(tokens) # XYZ -> (XY) = Z | (YX) = Z
        assert (rule[0] + rule[1]) not in combine
        assert (rule[1] + rule[0]) not in combine
        combine[rule[0] + rule[1]] = rule[2]
        combine[rule[1] + rule[0]] = rule[2]

    n_oppose = int(next(tokens))
    oppose = {}
    for n in range(n_oppose):
        rule = next(tokens) # XY -> X+Y = []
        assert rule[0] != rule[1]
        oppose[rule[0]] = rule[1]
        oppose[rule[1]] = rule[0]

    n_invoke = int(next(tokens))
    invoke = list(next(tokens))
    assert len(invoke) == n_invoke

    elements = ""
    
    while invoke:
        c = invoke[0]
        invoke = invoke[1:]
        elements += c
        if len(elements) == 1:
            continue
        pair = elements[-2:]
        if pair in combine:
            elements = elements[:-2] + combine[pair]
        elif (c in oppose) and (oppose[c] in set(elements)):
            elements = ""

    return elements


lines = (l.rstrip(os.linesep) for l in open("B-small-attempt4.in", "rt").xreadlines())
num_problems = int(next(lines))
lines = list(lines)
assert num_problems == len(lines)

out = open("output.txt", "wt")
for (n, line) in enumerate(lines):
    s = "Case #%d: [%s]\n" % (n+1, ", ".join(list(solve(line))))
    print s,
    out.write(s)

out.close()
              



