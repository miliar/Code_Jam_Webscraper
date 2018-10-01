from sys import exit, argv

f = open(argv[1])
lines = f.readlines()
f.close()

ncases =  int(lines[0])
c = 1
n = 1
while c<=ncases:
    nse = int(lines[n].strip())
    n+=1
    ses = []
    se = 0
    while se < nse:
        ses.append(lines[n].strip())
        n+=1
        se += 1
    nqu = int(lines[n].strip())
    n+=1
    qus = []
    qu = 0
    while qu < nqu:
        qus.append(lines[n].strip())
        n+=1
        qu += 1
    #print c
    #print ses
    #print qus
    ms = []
    h = {}
    
    for v1 in ses:
        m = [0]*nqu
        v = 0
        for v2 in qus:
            if v1==v2:
                m[v] = 1
            v += 1
        ms.append(m)
    #for m in ms:
    #    print m
    mask = [0]*nse
    cont = 0
    qu = 0
    atual = -1
    while qu < nqu:
        se = 0
        while se < nse:
            if ms[se][qu]==1:                
                mask[se] = 1
            if sum(mask)==nse and atual!=se:
                atual = se
                cont += 1
                mask = [0]*nse
                mask[se]=1
                break
            se += 1
            #print '*', mask, atual
        qu += 1
#    print cont, mask
#    if sum(mask)!=nse and sum(mask) > 1:
#        cont += 1
    print 'Case #' + str(c) +  ':', cont
    c+=1
    
