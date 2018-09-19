for i in range(1,input()+1):
    r,c,x=map(int,raw_input().split())
    print "Case #%d:"%(i),
    if c==x:
        print r-1+x
    elif x==1:
        print r*c
    else:
        print (r*((c-1)/x))+x
