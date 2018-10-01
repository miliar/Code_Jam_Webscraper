import sys
sys.setrecursionlimit(10000)

def read_line(f):
    while True:
        s=f.readline().strip()
        if s:
            return s
def read_list(f):
    return [int(x) for x in read_line(f).split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    N,_,M=read_tuple(f)
    tickets=[read_tuple(f) for _ in xrange(M)]
    return N,tickets


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases

# def solve2(N, tickets):
#     CTs={}
#     PTs={}
#     for p,b in tickets:
#         CTs[b]=CTs.get(b,0)+1
#         pCs=PTs.setdefault(p,{})
#         pCs[b]=pCs.get(b,0)+1
#     minR=max(CTs.values())
#     minup=0
#     for p in xrange(N):
#         if p in PTs:
#             pCs=PTs[p]
#             n1,n2=pCs.get(1,0),pCs.get(2,0)
#             if n1+n2>minR:
#                 minup

def findminRsim(N, tickets):
    CTs={}
    PTs={}
    for p,b in tickets:
        CTs[b]=CTs.get(b,0)+1
        pCs=PTs.setdefault(p,{})
        pCs[b]=pCs.get(b,0)+1
    minR=0
    minup=0
    Ntot=len(tickets)
    while Ntot>0:
        freeup=0
        custs=set()
        for p in xrange(N):
            if p not in PTs:
                freeup+=1
                continue
            pCs=PTs[p]
            added=0
            freetot=freeup+1
            for b in pCs.keys():
                if b not in custs:
                    pCs[b]-=1
                    if pCs[b]==0:
                        del pCs[b]
                    custs.add(b)
                    added+=1
                    if added==freetot:
                        break
            Ntot-=added
            if len(pCs)==0:
                del PTs[p]
            freeup=freetot-added
            if added>1:
                minup+=added-1
        minR+=1
    return minR,minup

def findminupsim(N, minR, tickets):
    CTs={}
    PTs={}
    for p,b in tickets:
        CTs[b]=CTs.get(b,0)+1
        pCs=PTs.setdefault(p,{})
        pCs[b]=pCs.get(b,0)+1
    minup=0
    for p in xrange(N):
        if p not in PTs:
            continue
        pCs=PTs[p]
        minup+=max(0,sum(pCs.values())-minR)
    return minup

def solveCsim(N, tickets):
    minR,minup=findminRsim(N,tickets)
    minup2=findminupsim(N,minR,tickets)
    return minR,minup2
    

def solve(case):
    N,tickets=case
    tickets=[(p-1,b) for (p,b) in tickets]
    return solveCsim(N,tickets)






def outcome_string(outcome):
    return "{} {}".format(*outcome)


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
    





########## SOLUTIONS TESTING ##########


def verify_outcome(case, outcome):
    ### IMPLEMENT ###
    return outcome==solve(case)

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
                
def gen_cases():
    ### IMPLEMENT ###
    return []

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