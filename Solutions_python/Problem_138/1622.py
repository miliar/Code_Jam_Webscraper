f = open('A-small-practice')
t = int(f.readline())
for r in range(1, t+1):
    n = int(f.readline())
    naomii = f.readline()
    keni = f.readline()
    naomi = sorted(list(map(float, naomii.split())))
    ken = sorted(list(map(float, keni.split())))
    nao = 0
    kenny = 0
    #print(ken)
    for rownd in range(0, n):
        good = True
        na = naomi.pop(0)
        ki = 0
        while ken[ki] < na:
            ki+=1
            if ki == len(ken):
                nao+=1
                ken.pop(0)
                good = False
                break
        if good:
            ken.pop(ki)
            kenny+=1
    #print(nao, kenny)
    naoc = 0
    kennyd = 0
    naomi = sorted(list(map(float, naomii.split())))
    ken = sorted(list(map(float, keni.split())))
    for rownd in range(0, n):
        good = True
        if naomi[-1]<ken[-1]:
            naomi.pop(0)
            ken.pop(-1)
            kennyd+=1
        else:
            naomi.pop(-1)
            ken.pop(-1)
            naoc+=1
    #print(naoc, nao)
    print('Case #{}: {} {}'.format(r, naoc, nao))





##        ki = 0
##        while ken[ki] < na:
##            ki+=1
##            if ki == len(ken):
##                nao+=1
##                ken.pop(0)
##                good = False
##                break
##        if good:
##            ken.pop(ki)
##            kenny+=1
    



##        d = c - p[j]
##        if p.count(d) and p.index(d) != j:
##            print('Case #{}: {} {}'.format(r, *(sorted([j+1, p.index(d)+1]))))
##            break
