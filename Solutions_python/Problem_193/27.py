import sys
from multiprocessing import Pool

# Add git repository with helpers to path
# The repo is publicly available at git@github.com:marcelka/cocoli.git
sys.path.append("/home/marcelka/projects/cocoli/")

def run(pool=None): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        arguments = []
        for _case in range(_cases):
            N = int(_file.readline()[:-1])
            knowledge = []
            for _ in range(N):
                knowledge.append(_file.readline()[:-1])
            arguments.append((_case + 1, (N, knowledge)))

        if pool == None:
            results = list(map(solve_wrapper, arguments))
        else:
            results = sorted(
                list(pool.imap_unordered(solve_wrapper, arguments)),
                key=lambda r: r[0])
        assert(len(results) == _cases)
        
        for _case, result in results:
            out.write("Case #%s: %s\n" % (_case, result))

def solve_wrapper(args):
    case_no, _args = args
    print("Solving case #%s" %(case_no))
    return (case_no, solve(*_args))
# }}}

from itertools import product, combinations, permutations

def can_cover(N, workers, know):
    res = set()
    options = product(range(N), repeat=len(workers))
    for o in options:
        if all(know[workers[i]][o[i]] == "1" for i in range(len(o))):
            if len(set(o)) == len(o):
                res.add(tuple(sorted(list(o))))
    return res

def is_ok2(N, after):
    for i in range(N + 1):
        for w1 in combinations(range(N), i):
            w2 = tuple(sorted(list(set(range(N)) - set(w1))))
            cc1 = can_cover(N, w1, after)
            cc2 = can_cover(N, w2, after)
            for c in cc1:
                c2 = tuple(sorted(list(set(range(N)) - set(c))))
                if c2 not in cc2:
                    return False
    return True

def solve(N, knowledge):
    positions = list(product(range(N), repeat=2))
    for i in range(N):
        for j in range(N):
            if knowledge[i][j] == "1":
                positions.remove((i, j))
    for dollars in range(N**2 + 1):
        for selected in combinations(positions, dollars):
            nk = [list(know) for know in knowledge]
            for i, j in selected:
                nk[i][j] = "1"
            if is_ok2(N, nk):
                return dollars
#def is_ok(N, after):
#    after2 = list(after)
#    while len(after2) > 0:
#        a = after2[0]
#        counta = after2.count(a)
#        if counta != a.count("1"):
#            return False
#        while a in after2:
#            after2.remove(a)
#    return True
#
#

#from union_find import union, find
#
#def solve(N, knowledge):
#    workers = dict((i, None) for i in range(N))
#    for j in range(N):
#        know = [i for i in range(N) if knowledge[i][j] == "1"]
#        if know:
#            for k in know[1:]:
#                union(workers, know[0], k)
#    groups = {}
#    for w1, w2 in workers.items():
#        if w2 == None: w2 = w1
#        if w2 not in groups: groups[w2] = set()
#        groups[w2].add(w1)
#
#    for _, g in groups.items():
#        group_knowledge = set()
#        for w in g:
#
#    while True:
#        done = []
#
#    blocks = []
#    return tpl, string, number

run()
#run(Pool(4))
