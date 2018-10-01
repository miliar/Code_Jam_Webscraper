from collections import defaultdict

f=open("input.txt")
cases=int(f.readline())
for i in xrange(0,cases):
    s_comb={}
    s_conf=defaultdict(list)
    n=f.readline().split(" ")
    ctr=0
    n_comb = int(n[ctr])
    for j in xrange(0,n_comb):
        ctr += 1
        comb=n[ctr]
        s_comb[(comb[0],comb[1])] = comb[2]
        s_comb[(comb[1],comb[0])] = comb[2]
    ctr+=1
    n_conf = int(n[ctr])
    for j in xrange(0,n_conf):
        ctr += 1
        conf=n[ctr]
        s_conf[conf[0]].append(conf[1])
        s_conf[conf[1]].append(conf[0])
    ctr+=1  
    n_inv = int(n[ctr])
    inv=[]
    ctr += 1
    inv_str=n[ctr]
    for x in inv_str[0:-1]:
        inv.append(x)
        if len(inv) > 1: # check combination
            last_elem = inv[-1:][0]
            second_last_elem = inv[-2:-1][0]
            if (last_elem,second_last_elem) in s_comb:
                inv.pop(); inv.pop()
                inv.append(s_comb[(last_elem,second_last_elem,)])
            else:
                for y in inv:
                    if y in s_conf[x]: inv=[]
    print "Case #%d: [%s]"%(i+1, ', '.join(inv))
f.close()