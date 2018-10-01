def calc(filename):
    f = open(filename,'r')
    L,D,N= f.readline().split()
    L=int(L)
    D=int(D)
    N=int(N)
    
    cases=[]
    for i in range(D):
       cases.append(f.readline().split()[0])
    
    ptns=[]
    for i in range(N):
        p = f.readline().split()[0]
        ptns.append([])
        j = 0
        while (j< len(p)):
            if p[j] == '(':
                ptns[i].append(p[j+1 : p.find(')',j+1)])
                j = p.find(')',j+1)+1
            else:
                ptns[i].append(p[j]) 
                j = j + 1
    print "PATTERNS:", ptns
    print "CASES:", cases
    
    res = []
    for k in range(N):
        res.append(0)

    for d in range(D):
        word = cases[d]
        for n in range(N):
            flag = 'T'
            for l in range(L):
                if (ptns[n][l].find(word[l],0) == -1):
                    flag = 'F'
                    break    
            if flag == 'T':
                res[n] = res[n]+1
    print "RESULT:", res

    out = open('A-large.out','w')
    for n in range(N):
        out.write("Case #"+str((n+1))+": "+str(res[n])+"\n") 

def m():
    calc('A-large.in')
