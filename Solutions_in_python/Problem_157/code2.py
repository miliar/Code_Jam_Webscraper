inf = open('C-small-attempt3.in')
cases = inf.readline().strip()
out = open('out2.dat','w')

M = dict()
M[('1','1')] = '+11'; M[('1','i')] = '+1i'
M[('1','j')] = '+1j'; M[('1','k')] = '+1k'

M[('i','1')] = '+1i'; M[('i','i')] = '-11'
M[('i','j')] = '+1k'; M[('i','k')] = '-1j'

M[('j','1')] = '+1j'; M[('j','i')] = '-1k'
M[('j','j')] = '-11'; M[('j','k')] = '+1i'

M[('k','1')] = '+1k'; M[('k','i')] = '+1j'
M[('k','j')] = '-1i'; M[('k','k')] = '-11'

D=dict()

D['1'] = '-1i'; D['i'] = '+11'
D['j'] = '-1k'; D['k'] = '+1j'


def mult(x,y):
    es = int(x[0:2])*int(y[0:2])
    r = M[(x[2],y[2])]
    es = es*int(r[0:2])
    if es>0:
        return '+1'+r[2]
    else:
        return '-1'+r[2]

def divi(r):
    s = int(r[0:2])
    sm = D[r[2]]
    s = s*int(sm[0:2])
    if s>0:
        return '+1'+sm[2]
    else:
        return '-1'+sm[2]
    
    
for case in range(int(cases)):
    
    spline = inf.readline().strip().split(' ')
    L = int(spline[0])
    X = int(spline[1])

    #reduce X
    if X > 8:
        X = 8+X%4

    #final string
    S = inf.readline().strip()*X

    exists = False

    #save acum, i indexes
    i_indexes = []
    n=0
    ac = '+11'
    acum = []
    for l in S:
        ac = mult(ac,'+1'+l)
        acum.append(ac)
        if ac == '+1i':
            i_indexes.append(n)
        n+=1
        
    k_indexes = []
    #save k indexes
    n = len(S)-1
    ac = '+11'
    while n>=2:
        ac = mult('+1'+S[n],ac)
        if ac=='+1k':
            k_indexes.append((n,acum[n-1]))
        n-=1

    k_indexes.reverse()
    #find matches
    i=0
    min_k = 0
    K = len(k_indexes)
    while i<len(i_indexes):
        k = min_k
        while k < K:
            (ind,pval) = k_indexes[k]
            if ind<=i+1:
                min_k = k
            elif divi(pval)=='+1j':
                exists = True
                break
            k+=1
        if exists:
            break
        i+=1
    
    if exists:
        out.write("Case #"+str(case+1)+": YES\n")
    else:
        out.write("Case #"+str(case+1)+": NO\n")

out.close()
