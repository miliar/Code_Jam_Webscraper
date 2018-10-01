T = input()

TT = int(T)

def solve (C , F , X , E, R):
    falta = (X-C)/(2+E)
    faltaria = X/(2+E+F)
    if (faltaria < falta):
        R += C/(2+E+F)
        return solve(C,F,X,E+F,R)
    else:
        R += (X-C)/(2+E)
        return R

def solve2 (C, F, X, E , R):
    falta = (X-C)/(2+E)
    faltaria = X/(2+E+F)
    resp = 0;
    while(faltaria < falta):
        E += F
        resp += C/(2+E)
        falta = (X-C)/(2+E)
        faltaria = X/(2+E+F)
    resp += (X-C)/(2+E)
    return resp
    
    
    
    
for j in range(TT):
    r1 = input()
    r1 = r1.split()
    C = float(r1[0])
    F = float(r1[1])
    X = float(r1[2])
    time = 1
    extra = 0
    mount = 2*time
    res = 0
    if(C/2 < X/2):
        reus = solve2(C, F, X, 0 , 0)
        print("Case #%d: %.7f" % (j+1 , reus + C/2))
    else :
        print("Case #%d: %.7f" %(j+1 , X/2))
        