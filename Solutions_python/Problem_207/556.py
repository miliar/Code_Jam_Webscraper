T = int(raw_input())
for t in range(T):
    N, R, O, Y, G, B, V = [int(i) for i in raw_input().split()]
    nn=N
    rr=R
    oo=O
    yy=Y
    gg=G
    bb=B
    vv=V
    
    count=0

    if rr>0:
        count=count+1
    if O>0:
        count=count+1
    if Y>0:
        count=count+1
    if G>0:
        count=count+1
    if B>0:
        count=count+1
    if V>0:
        count=count+1
    #print yy,vv, count
    impossible=False
    ba=[]
    ra=[]
    ya=[]
    while O>0:
        if B>=2:
            O=O-1
            B=B-2
            ba.append("BOB")
        else:
            impossible=True
            #print "impossible bob"
            break
    while G>0:
        if R>=2:
            G=G-1
            R=R-2
            ra.append("RGR")
        else:
            impossible=True
            #print "impossible rgr"
            break
    while V>0:
        if Y>=2:
            V=V-1
            Y=Y-2
            ya.append("YVY")
        else:
            impossible=True
            #print "impossible yvy"
            break
            
    maksi = B
    for i in range(B):
        ba.append("B")
    for i in range(R):
        ra.append("R")
    for i in range(Y):

        ya.append("Y")

    z=[ba,ra,ya]
    
 
    sz = sorted(z,key=lambda x:len(x), reverse=True)
    total = len(ba)+len(ra)+len(ya)
   
    rv=""
    #print z
    if len(sz[0])>len(sz[1])+len(sz[2]):
        impossible=True
        #print "impossible prelom"
    if not impossible:
        for i in range(total):
            if i%2==0 and len(sz[0])>0:
                rv=rv+sz[0].pop()
            else :
                if len(sz[1])>=len(sz[2]):
                    rv=rv+sz[1].pop()
                else:
                    rv=rv+sz[2].pop()
            
        
    
    if impossible:
        if count==2:
            if vv>0 and yy>0 and vv==yy:
                impossible=False
                for i in range(vv):
                    rv+="VY"
            if gg>0 and rr>0 and rr==gg:
                impossible=False
                for i in range(gg):
                    rv+="RG"
            if oo>0 and bb>0 and bb==oo:
                impossible=False
                for i in range(bb):
                    rv+="BO"
        
    if impossible:
        print "Case #%d: IMPOSSIBLE" %(t+1)
    else:
        print "Case #%d: %s" % (t+1, rv)
    
