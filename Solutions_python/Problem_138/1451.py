def dwar(n,k):
    c = 0
    while (n!=[]) :
        if k[0] < n.pop(0) :
            k.pop(0)
            c += 1
        else :
            k.pop()
    return c

def war(n,k):
    c = 0
    while (n!=[]) :
        cn = n.pop()
        if k[len(k)-1] < cn :
            k.pop(0)
            c += 1
        else :
            k.remove(min(x for x in k if x > cn))
    return c

f = open('D-large.in','r')
n = int(f.readline())
cases = []
for i in range(n):
    m=f.readline()
    naomi,ken = [],[]
    for j in f.readline().split() : naomi.append(float(j))
    for k in f.readline().split() : ken.append(float(k))
    naomi.sort()
    ken.sort()
    x = dwar(naomi[:],ken[:])
    y = war(naomi[:],ken[:])
    cases.append('Case #'+`i+1`+': '+`x`+' '+`y`)
f.close()
g = open('outputD.txt','w')
for z in cases :
    g.write(z+'\n')
g.close()