#k[n] > n[n] = pointK, del k[0] n[n]
#k[n] < n[n] = pointN, del k[n] n[n]

#n[0] > k[0] del k[n] n[0] PointN
#n[0] < k[0] del k[0] n[0] PointK

import time
t = time.clock()
#f = open('Block-Test.txt')
#f = open('Block-Small.txt')
f = open('Block-Large.txt')
#out = open('Block-Test-Out.txt','w+')
#out = open('Block-Small-Out.txt','w+')
out = open('Block-Large-Out.txt','w+')

def war (N,K,nS,nE,kS,kE):
    if N[nS] > K[kS]:
        return nS+1,nE,kS,kE-1,1,0
    return nS+1,nE,kS+1,kE,0,1
    

def decWar(N,K,nS,nE,kS,kE):
    if K[kE] > N[nE]:
        return nS,nE-1,kS+1,kE,0,1
    return nS,nE-1,kS,kE-1,1,0

def warGo(N,K,isDec):
    nS,nE,kS,kE,pN,pK = (0,len(N)-1,0,len(K)-1,0,0)
    for i in range(len(N)):
        nS,nE,kS,kE,pDN,pDK = decWar(N,K,nS,nE,kS,kE) if isDec else war(N,K,nS,nE,kS,kE)
        pK += pDK
        pN += pDN
    return pN

def func(caseI,gen):
    count = int(gen.next())
    N = [float(f) for f in gen.next().split(' ')[:count]]
    K = [float(f) for f in gen.next().split(' ')[:count]]
    N.sort()
    N.reverse()
    K.sort()
    K.reverse()
    d,w = (warGo(N,K,True),warGo(N,K,False))
    return 'Case #' + str(caseI+1)+": " + str(d) + " " + str(w)

lines = f.read().split('\n')
cases = int(lines[0])
gen = (l for l in lines[1:])
for i in range(cases):
    out.write(func(i,gen)+'\n')
out.close()
f.close()

print time.clock() - t
