def load_single_case(f):
    [N,M]=[int(n) for n in f.readline().split()]
    return (N,M)


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases




def get_max_losses(N,r):
    l=0
    while r>0:
        r=(r-1)/2
        l=l+1
    return l
def get_needed_losses(N,M):
    if M==2**(N)-1:
        return N
    l=0
    h=2**(N-1)
    while M>=h:
        M=M-h
        h=h/2
        l=l+1
    return l+1


def get_max_wins(N,r):
    r=2**N-1-r
    l=0
    while r>0:
        r=(r-1)/2
        l=l+1
    return l
def get_needed_wins(N,M):
    if M==0:
        return N
    w=0
    h=2**(N-1)
    while M<h:
        h=h/2
        w=w+1
    return w+1


def binsearch_leq(f, x, l, r): # lst is ascending, so f(l)<=x<=f(r)
    if r==None:
        r=len(lst)-1
    if f(r)<=x:
        return r
    if f(l)>=x or (r-l<2):
        return l
    m=(l+r)/2
    if f(m)<x:
        return binsearch_leq(f,x,m,r)
    else:
        return binsearch_leq(f,x,l,m)

def solve(case):
    N,M=case
    M=M-1
    if M<=0:
        return (0,0)
    if M==2**N-1:
        return (2**N-1,2**N-1)
    needed_losses=get_needed_losses(N,M)
    needed_wins=get_needed_wins(N,M+1)
    g=binsearch_leq(lambda r: get_max_losses(N,r), needed_losses, 0, 2**N-1)-1
    p=binsearch_leq(lambda r: -get_max_wins(N,r), -needed_wins, 0, 2**N-1)+1
    return (g,p)
    
     






def outcome_string(outcome):
    return "{0} {1}".format(*outcome)


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