import sys
import itertools
import pdb

from collections import namedtuple

Problem = namedtuple('Problem','n surprises max_p scores')

score = [0,10]

def gen_triples():
    for x in range(score[0],score[1]):
        yield (x,x,x)
        yield (x,x,x+1)
        yield (x,x+1,x+1)

    x = score[1]
    yield (x,x,x)

sums_t = [ (sum(t),t) for t in gen_triples() ]

sm = dict(sums_t)

def gen_sup_triples():
    for x in range(score[0],score[1]-1):
        yield (x,x,x+2)
        yield (x,x+1,x+2)
        yield (x,x+2,x+2)

sums_st = [ (sum(t),t) for t in gen_sup_triples() ]

sup_m = dict(sums_st)

def base(scores):
    return [ sm[s] for s in scores ]


def gen_solutions(scores,surprises):
    indexes = itertools.combinations(range(len(scores)),surprises)
    for replacement_list in indexes:
        b = base(scores)
        valid = True
        for replacment in replacement_list:
            try:
                b[replacment] = sup_m[sum(b[replacment])]
            except KeyError, e:
                # cannot have a surprising result in this position
                valid = False
        if valid:
            yield b

def count_solutions(solutions,max_p):
    """max number of people out all the solutions with an individual score >= max_p"""

    pmax_list = []
    for solution in solutions:
        pmax_list.append(len(list(1 for t in solution if max(t) >= max_p)))
    return max(pmax_list)


def parse_problem(line):
    n, s, p, vals  = line.split(' ',3)
    problem = Problem(int(n),int(s),int(p),[ int(score)  for score in vals.split(' ')])
    assert problem.n == len(problem.scores)
    return problem

def util_process_line(line):
    problem = parse_problem(line)
    solutions = gen_solutions(problem.scores,problem.surprises)
    c = count_solutions(solutions,problem.max_p)
    return c


if __name__ == "__main__":
    f = open(sys.argv[1])
    cases = int(f.next())
    lines = [ f.next().strip() for _ in range(cases) ]
    for i,v in enumerate(lines):
        print "Case #%d: %s" % (i+1,util_process_line(v))