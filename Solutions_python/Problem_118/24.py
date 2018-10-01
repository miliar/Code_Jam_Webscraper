# author: misof
# language: python

def comb(n,k):
    res=1
    for i in range(1,k+1): res = (res*(n-i+1))//i
    return res

count_len = [0,3]
for l in range(2,107):
    poz=(l//2)-1
    if l%2==0:
        c=1
        for v in range(4): c+=comb(poz,v)
    else:
        c=2
        for s in [2,3,6]:
            mv=(9-s)//2
            for v in range(mv+1): c+=comb(poz,v)
    count_len.append(c)

def sucet(cislo):
    return cislo.count('1') + 4*cislo.count('2') + 9*cislo.count('3')

def dopln_na_najmensi(prefix):
    global sqrtX
    chyba = len(sqrtX) - 2*len(prefix)
    if chyba >= 0: return prefix + ('0'*chyba) + prefix[::-1]
    zober = len(sqrtX) - len(prefix)
    return prefix + prefix[:zober][::-1]

def dopln_na_najvacsi(prefix):
    global sqrtX
    if 2*len(prefix)>=len(sqrtX):
        zober = len(sqrtX) - len(prefix)
        return prefix + prefix[:zober][::-1]
    
    pouzil = 2*sucet(prefix)
    ostava = 9-pouzil
    if 2*len(prefix)+1==len(sqrtX):
        stred='0'
        if ostava>=1: stred='1'
        if ostava>=4: stred='2'
        return prefix+stred+prefix[::-1]

    if ostava>=2: return dopln_na_najvacsi(prefix+'1')
    pol=len(sqrtX)//2
    return dopln_na_najvacsi(prefix+('0'*(pol-len(prefix))))

def sposobov_doplnenia(prefix):
    global sqrtX
    if 2*len(prefix)>=len(sqrtX): return 1
    pouzil = 2*sucet(prefix)
    ostava = 9-pouzil
    volne = (len(sqrtX)//2) - len(prefix)
    ans = 0
    if len(sqrtX)%2==0:
        mv = ostava//2
        for v in range(mv+1): ans += comb(volne,v)
    else:
        ans = 0
        for s in range(3):
            if s*s > ostava: continue
            mv = (ostava-s*s)//2
            for v in range(mv+1): ans += comb(volne,v)
    return ans

def solve(prefix):
    global sqrtX
    # mozno je prefix privelky
    najmensi = dopln_na_najmensi(prefix)
    if 2*len(prefix)<=len(sqrtX) and 2*sucet(prefix)>9: return 0
    if sucet(najmensi) > 9: return 0
    if najmensi > sqrtX: return 0
    # mozno je prefix primaly
    najvacsi = dopln_na_najvacsi(prefix)
    if najvacsi <= sqrtX:
        return sposobov_doplnenia(prefix)
    # ak si tu, skus vsetky moznosti pre dalsiu cifru
    if 2*len(prefix)<len(sqrtX): return solve(prefix+'0') + solve(prefix+'1') + solve(prefix+'2')
    chyba = len(sqrtX) - len(prefix)
    return solve(prefix+prefix[chyba-1])

def rataj():
    global X, sqrtX
    lo,hi = 0,X+1
    while hi-lo>1:
        med=(hi+lo)//2
        if med**2 <= X: lo=med
        else: hi=med
    sqrtX = str(lo)
    answer = 0
    for i in range(1,len(sqrtX)): answer += count_len[i]
    answer += solve('1')
    answer += solve('2')
    answer += solve('3')
    return answer

T = int(input())
for t in range(1,T+1):
    A, B = [ int(x) for x in input().split() ]
    X = B
    dobre = rataj()
    X = A-1
    zle = rataj()
    print('Case #{}: {}'.format(t,dobre-zle))
