t = int(raw_input())  # read a line with a single integer
for numtest in xrange(1, t + 1):
    n,p=[int(k) for k in raw_input().split(" ")] 
    g=[int(k) for k in raw_input().split(" ")]
    res=0
    nb=[0]*p
    for i in g:
        ii=i%p
        nb[ii]+=1
    if p==2:
        res+=nb[0]+(nb[1]-nb[1]/2)
    elif p==3:
        res+=nb[0]
        nbc=min(nb[1],nb[2])
        res+=nbc
        left=max(nb[1],nb[2])-nbc
        res+=left-(left*2)/3
    elif p==4:
        res+=nb[0]
        nb2=nb[2]/2
        res+=nb2
        nb13=min(nb[1],nb[3])
        res+=nb13
        left=[0,nb[1]-nb13,nb[2]%2,nb[3]-nb13]
        w=0
        if nb[1]>nb13:
            w=1
        if nb[3]>nb13:
            w=3
            #handling last 2
        if left[2]>0 and max(left)>1:
            leftt=[0]*4
            leftt[w]=nb[w]-nb13-2
            res+=1
        else:
            leftt=left
        #then group by 4
        #res+=leftt[w]-(leftt[w]*3/4)
        res+=sum(leftt)-(sum(leftt)*3/4)             
    print "Case #{}: {}".format(numtest,res)
