# case === (a,b)
def load_single_case(f):
    return [int(n) for n in f.readline().split()]
def load_cases(path):
    with open(path) as f:
        n=int(f.readline())
        cases=[]
        for _ in xrange(n):
            cases.append(load_single_case(f))
    return cases


def is_palindrome(n):
    s=str(n)
    return s==s[::-1]
def build_palindrome(sn,l):
    if l%2==1:
        return int(sn+sn[-2::-1])
    else:
        return int(sn+sn[::-1])
    
def try_add(sn,lst,l):
    p=build_palindrome(sn,l)
    if is_palindrome(p*p):
        lst.append(p)                
def build_palindrome_list(l):
    if l==1:
        return [1,2,3]
    elif l==2:
        return [11,22]
    lst=[]
    for n in xrange(2**((l-1)/2),2**((l+1)/2)):
        sn=bin(n)[2:]
        try_add(sn,lst,l)
        try_add('2'+sn[1:],lst,l)
        if n%2==1:
            try_add(sn[:-1]+'2',lst,l)
    return lst
def build_complete_palindrome_list(l):
    lst=[]
    for i in range(1,l+1):
        lst=lst+build_palindrome_list(i)
    return lst
pali_list=build_complete_palindrome_list(50)
sq_pali_list=[p**2 for p in pali_list]

def get_fsqn(case):
    n=0
    for x in sq_pali_list:
        if x>=case[0] and x<=case[1]:
            n=n+1
    return n


def save_outcomes(path, outcomes):
    with open(path,'w') as f:
        for n,o in enumerate(outcomes):
            f.write("Case #{0}: {1}\n".format(n+1,o))

def process(path_in, path_out):
    cases=load_cases(path_in)
    outcomes=[get_fsqn(c) for c in cases]
    save_outcomes(path_out, outcomes)