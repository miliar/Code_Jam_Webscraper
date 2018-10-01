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
    R,_=read_tuple(f)
    grid=[read_line(f) for _ in xrange(R)]
    return grid


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases


rotd={  "/" :{ (1,0):(0,-1), (-1,0):(0, 1), (0,1):(-1,0), (0,-1):( 1,0) },
        "\\":{ (1,0):(0, 1), (-1,0):(0,-1), (0,1):( 1,0), (0,-1):(-1,0) }  }
def prop_beam(pos, d, grid):
    R,C=len(grid),len(grid[0])
    filled=[[False]*C for _ in xrange(R)]
    while True:
        pos=(pos[0]+d[0],pos[1]+d[1])
        if pos[0]<0 or pos[0]>=R or pos[1]<0 or pos[1]>=C: #OOB
            break
        ncell=grid[pos[0]][pos[1]]
        if ncell=="#":
            break
        if ncell in "-|":
            return None
        if ncell==".":
            filled[pos[0]][pos[1]]=True
        if ncell in "/\\":
            d=rotd[ncell][d]
    return filled
def test_laser(pos, grid, ecs):
    assert grid[pos[0]][pos[1]] in "-|"
    td=prop_beam(pos,( 1,0),grid)
    tu=prop_beam(pos,(-1,0),grid)
    if (tu is None) or (td is None):
        tv=None
    else:
        tv=[ (td[ec[0]][ec[1]] or tu[ec[0]][ec[1]]) for ec in ecs ]
    tr=prop_beam(pos,(0, 1),grid)
    tl=prop_beam(pos,(0,-1),grid)
    if (tr is None) or (tl is None):
        th=None
    else:
        th=[ (tr[ec[0]][ec[1]] or tl[ec[0]][ec[1]]) for ec in ecs ]
    return tv,th


def combine_lasers_bf(eus, fts):
    if len(fts)==0:
        return [] if all(eus) else None
    t=fts[0]
    eusv=[(e or te) for e,te in zip(eus,t[0])]
    cv=combine_lasers_bf(eusv, fts[1:])
    if cv is not None:
        return [0]+cv
    eush=[(e or te) for e,te in zip(eus,t[1])]
    ch=combine_lasers_bf(eush, fts[1:])
    if ch is not None:
        return [1]+ch
    return None


def apply_constraints(sats, rule):
    l,p=rule
    np="|" if p=="-" else "-"
    csats=[]
    for s in sats:
        s=s.copy()
        if (l,p) in s:
            continue
        if (l,np) in s:
            s.remove((l,np))
        csats.append(s)
    return csats
        
def df_constraints(sats):
    if len(sats)==0:
        return []
    nvars=[len(s) for s in sats]
    minnvar=min(nvars)
    if minnvar==0:
        return None
    minidx=nvars.index(minnvar)
    minsat=sats[minidx]
    for r in minsat:
        nsats=apply_constraints(sats,r)
        newcons=df_constraints(nsats)
        if newcons is not None:
            return newcons+[r]
    return None
def combine_lasers_br(eus, fts):
    ffts=[]
    for ft in fts:
        ftv=[ te for (te,ee) in zip(ft[0],eus) if not ee]
        fth=[ te for (te,ee) in zip(ft[1],eus) if not ee]
        ffts.append((ftv,fth))
    eus=[e for e in eus if not e]
#     print ffts,eus
    sats=[]
    for i in xrange(len(eus)):
        sats.append(set())
        for l,ft in enumerate(fts):
#             print i,l,ft
            if ft[0][i]:
                sats[i].add((l,"|"))
            if ft[1][i]:
                sats[i].add((l,"-"))
#     print sats
    cs=df_constraints(sats)
    if cs is None:
        return None
#     print cs
    dirs=[0]*len(ffts)
    for c in cs:
        if c[1]=="|":
            dirs[c[0]]=1
    return dirs



def combine_lasers(tests):
    eus=[False]*len(tests[0][0])
    fts=[]
    for t in tests:
        if len(t)==1:
            eus=[(e or te) for e,te in zip(eus,t[0])]
        else:
            fts.append(t)
    return combine_lasers_br(eus,fts)





def solve(case):
    grid=case
    R,C=len(grid),len(grid[0])
    ecs=[]
    lcs=[]
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j]==".":
                ecs.append((i,j))
            if grid[i][j] in "-|":
                lcs.append((i,j))
#     print "New", grid
    lts=[]
    lps=[]
    for l in lcs:
        lt=test_laser(l,grid,ecs)
        if lt[0] is None and lt[1] is None:
            return None
        if lt[0] is None:
            lts.append((lt[1],))
            lps.append("-")
        elif lt[1] is None:
            lts.append((lt[0],))
            lps.append("|")
        else:
            lts.append(lt)
            lps.append("-|")
    dirs=combine_lasers(lts)
    if dirs is None:
        return None
    nd=0
    lpds=[]
    for i,p in enumerate(lps):
        if len(p)==1:
            lpds.append(p)
        else:
            lpds.append(p[dirs[nd]])
            nd+=1
    assert nd==len(dirs)
    grid=[list(r) for r in grid]
    for p,d in zip(lcs,lpds):
        grid[p[0]][p[1]]=d
    return grid






def outcome_string(outcome):
    if outcome is None:
        return "IMPOSSIBLE"
    grid="\n".join([ "".join(r) for r in outcome ])
    return "POSSIBLE\n"+grid


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