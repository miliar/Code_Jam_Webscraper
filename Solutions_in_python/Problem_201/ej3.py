import random

def iniciar():
    archivo = open("ej.txt", "r") 
    t = archivo.readline()
    t = int(t)
    for i in range(1, t+1):
        ej = archivo.readline()
        result = resolver(ej)
        print "Case #" + str(i) + ": " + str(result)

def resolver(ej):
    n = ej.split(" ")[0] 
    k = ej.split(" ")[1] 

    # print c
    # print k
    n = int(n)
    k = int(k)
    
    l = list(x-1 for x in range(0, n+2))
    l[n+1] = -1
    r = list(x-1 for x in range(n+1, -1, -1))
    r[0] = -1
    mini = map(min,zip(l,r))

    # print l
    # print r
    # print mini
    
    for per in range(0,k):
        max_val = max(mini)
        # print "max val " + str(max_val)
        maxi_index = [elem for elem in range(0,len(mini)) if mini[elem] == max_val]
        # print "maxi index " + str(maxi_index)
        if len(maxi_index) == 1:
            ocupa = maxi_index[0]
            # print "ocupa " + str(ocupa)
        else:
            zipped = zip(l,r)
            # print "zipped "+ str(zipped)
            zipped2 = [zipped[i] for i in maxi_index]
            # print "zipped2 "+ str(zipped2)
            maxi = map(max,zipped2)
            # print "maxi "+ str(maxi)

            # print maxi_index[maxi.index(max(maxi))]
            ocupa = maxi_index[maxi.index(max(maxi))]
        
        res_max = max(l[ocupa], r[ocupa])
        res_min = min(l[ocupa], r[ocupa])
        l[ocupa] = -1
        for act in range(ocupa+1,n+1):
            if l[act] == -1:
                break 
            l[act] = l[act-1]+1
        r[ocupa] = -1
        for act in range(ocupa-1,0,-1):
            if r[act] == -1:
                break 
            r[act] = r[act+1]+1
        mini = map(min,zip(l,r))
        # print l
        # print r
        # print mini
    mini = map(min,zip(l,r))
    maxi = map(max,zip(l,r))
    return str(res_max) + " " + str(res_min)
    # for x in xrange(0,k):
        

iniciar() 
