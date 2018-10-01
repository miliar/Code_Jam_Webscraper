def read_list(f):
    return [int(x) for x in f.readline().split()]
def read_tuple(f):
    return tuple(read_list(f))

def load_single_case(f):
    N,=read_tuple(f)
    sent=[set(f.readline().strip().split()) for _ in xrange(N)]
    return sent


def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
        #for _ in xrange(15):
            cases.append(load_single_case(f))
    return cases




'''def build_graph(sent):
    gr={}
    all_words=set.union(*sent)
    w_idx={}
    n=len(sent)
    for w in all_words:
        w_idx[w]=n
        n=n+2
    for i in xrange(len(sent)):
        for j in xrange(i+1,len(sent)):
            ovl=len(set.intersection(sent[i],sent[j]))
            if ovl>0:
                gr.setdefault(i,{})[j]=[0,ovl]
                gr.setdefault(j,{})[i]=[0,ovl]
    return gr
def bf(gr, u, v):
    border={u:[u]}
    visited={u}
    while border:
        new_border={}
        for x,p in border.iteritems():
            for y,e in gr[x].iteritems():
                cf=e[1]-e[0]
                if cf>0:
                    if y==v:
                        return p+[v]
                    if y not in visited:
                        visited.add(y)
                        new_border[y]=p+[y]
        border=new_border
    return None
def upd_cf(gr, path):
    cfmin=None
    for i in xrange(len(path)-1):
        u,v=path[i],path[i+1]
        cf=gr[u][v][1]-gr[u][v][0]
        if cfmin is None:
            cfmin=cf
        else:
            cfmin=min(cfmin,cf)
    for i in xrange(len(path)-1):
        u,v=path[i],path[i+1]
        gr[u][v][0]=gr[u][v][0]+cfmin
        gr[v][u][0]=gr[v][u][0]-cfmin
def tot_flow(gr, x):
    if not x in gr:
        return 0
    f=0
    for e in gr[x].itervalues():
       f=f+e[0]
    return f 
def ffa(gr):
    while True:
        path=bf(gr,0,1)
        if path is None:
            return tot_flow(gr,0)
        print path
        upd_cf(gr,path)

def solve(case):
    sent=case
    #print sent
    gr=build_graph(sent)
    print gr
    return ffa(gr)'''

        
     
def clean_words(sent):
    ovlap=set.intersection(sent[0],sent[1])
    for o in ovlap:
        for s in sent:
            if o in s:
                s.remove(o)
    return len(ovlap)
def idx(sent):
    all_words=set.union(*sent)
    w_idx={}
    n=0
    for w in all_words:
        w_idx[w]=n
        n=n+1
    return [ set([w_idx[w] for w in s]) for s in sent ]

def get_ovlap(s1,s2):
    return len(set.intersection(set.union(*s1),set.union(*s2)))

def check_all_ovlap(s1,s2,ws):
    if len(ws)==0:
        return len(set.intersection(s1,s2))
    else:
        w=ws[0]
        ws=ws[1:]
        return min(check_all_ovlap(s1.union(w),s2,ws),check_all_ovlap(s1,s2.union(w),ws))

def solve(case):
    print len(case)
    sent=case
    o=clean_words(sent)
    sent=idx(sent)
    return o+check_all_ovlap(sent[0],sent[1],sent[2:])






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