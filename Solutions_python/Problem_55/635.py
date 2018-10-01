f=open('C-small-attempt0.in', 'r')
T=int(f.readline());

for casecount in xrange(1,T+1):
    l1=f.readline();
    l1=l1.split()
    R=int(l1[0])
    k=int(l1[1])
    N=int(l1[2])
    l2=f.readline()
    l2=l2.split()
    g=map(lambda x:int(x),l2)

    c=0
    for i in xrange(1,1+R):
        kcount=0
        Coaster=[]
        while True:
            if len(g)>0 and kcount+g[0]<=k:
                kcount+=g[0]
                Coaster.append(g[0])
                g=g[1:]
            else:
                break
        c+=kcount 
        g=g+Coaster
    print "Case #%d: %d" % (casecount, c)

f.close()
