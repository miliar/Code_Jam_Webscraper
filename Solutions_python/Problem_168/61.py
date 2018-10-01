def read_list(f):
    return [int(x) for x in f.readline().split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    R,C=read_tuple(f)
    grid=[]
    for _ in xrange(R):
        ln=f.readline().strip()
        assert len(ln)==C
        grid.append(ln)
    return grid


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def check_place_dir_slow(grid, p, d):
    R,C=len(grid),len(grid[0])
    r,c=p[0]+d[0],p[1]+d[1]
    while (r>=0) and (r<R) and (c>=0) and (c<C):
        if grid[r][c]!=".":
            return True
        r,c=r+d[0],c+d[1]
    return False 

arrow_dirs={">":(0,1),"<":(0,-1),"^":(-1,0),"v":(1,0)}
def check_place_slow(grid, p):
    r,c=p
    if grid[r][c]==".":
        return 0
    arr=arrow_dirs[grid[r][c]]
    if check_place_dir_slow(grid,p,arr):
        return 0
    for d in arrow_dirs.itervalues():
        if check_place_dir_slow(grid,p,d):
            return 1
    return None

def solve_slow(case):
    grid=case
    R,C=len(grid),len(grid[0])
    s=0
    for r in xrange(R):
        for c in xrange(C):
            res=check_place_slow(grid,(r,c))
            if res is None:
                return None
            s=s+res     
    return s




def check_place_dir(grid, p, d, costs):
    if p not in costs[d]:
        R,C=len(grid),len(grid[0])
        r,c=p[0]+d[0],p[1]+d[1]
        res=False
        while (r>=0) and (r<R) and (c>=0) and (c<C):
            if grid[r][c]!=".":
                res=True
            r,c=r+d[0],c+d[1]
        costs[d][p]=res
    return costs[d][p]

arrow_dirs={">":(0,1),"<":(0,-1),"^":(-1,0),"v":(1,0)}
def check_place(grid, p, costs):
    r,c=p
    if grid[r][c]==".":
        return 0
    arr=arrow_dirs[grid[r][c]]
    if check_place_dir(grid,p,arr,costs):
        return 0
    for d in arrow_dirs.itervalues():
        if check_place_dir(grid,p,d,costs):
            return 1
    return None

def solve(case):
    grid=case
    R,C=len(grid),len(grid[0])
    s=0
    costs=dict([(d,{}) for d in arrow_dirs.itervalues()])
    for r in xrange(R):
        for c in xrange(C):
            res=check_place(grid,(r,c),costs)
            if res is None:
                return None
            s=s+res     
    return s






def outcome_string(outcome):
    if outcome is None:
        return "IMPOSSIBLE"
    return "{}".format(outcome)


def save_outcomes(path, outcomes):
    with open(path,'w') as f:
        for n,o in enumerate(outcomes):
                f.write("Case #{0}: {1}\n".format( n+1 , outcome_string(o) ))
def process(path_in, path_out=None):
    if path_out==None:
        path_out=path_in.rsplit(".",1)[0]+".out"
    cases=load_cases(path_in)
    outcomes=[solve(c) for c in cases]
    save_outcomes(path_out, outcomes)
    




def verify_outcome(case, outcome):
    #return outcome==solve_slow(case)
    return True

def test_solutions(path_in, until_first_fail=True):
    cases=load_cases(path_in)
    for cn,c in enumerate(cases):
        o=solve(c)
        if not verify_outcome(c,o):
            print "Wrong outcome!"
            print "Case #{0}:".format(cn)
            print c
            print "Outcome:"
            print o
            if until_first_fail:
                return c
            else:
                print "\n\n"

def gc():
    R,C=100,100
    sels="......><v^"
    l=len(sels)
    return [ "".join([sels[randint(l)] for _ in xrange(C)]) for _ in xrange(R)]
def gen_cases():
    return [gc() for _ in xrange(10)]

def test_solutions_gen(until_first_fail=True):
    cases=gen_cases()
    for cn,c in enumerate(cases):
        o=solve(c)
        if not verify_outcome(c,o):
            print "Wrong outcome!"
            print "Case #{0}:".format(cn)
            print c
            print "Outcome:"
            print o
            if until_first_fail:
                return c
            else:
                print "\n\n"