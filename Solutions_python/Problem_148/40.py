def read_list(f):
    return [int(x) for x in f.readline().split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    _,X=read_tuple(f)
    si=read_list(f)
    return X,si


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def solve_bf(case):
    X,si=case
    si=sorted(si)
    n=0
    while len(si)>0:
        a1=si[0]
        si=si[1:]
        p2=None
        for i2,a2 in enumerate(si):
            if a1+a2<=X:
                p2=i2
        if p2!=None:
            si=si[:p2]+si[p2+1:]
        n=n+1
    return n

def solve_lin(X,si):
    si=sorted(si)
    n=0
    s=0
    f=len(si)-1
    while s<f:
        if si[s]+si[f]<=X:
            s=s+1
            f=f-1
        else:
            f=f-1
        n=n+1
    if s==f:
        n=n+1
    return n

def solve(case):
    X,si=case
    return solve_lin(X,si)





def outcome_string(outcome):
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