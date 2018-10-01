T = int(raw_input())
import sys
sys.setrecursionlimit(100000)
def fill_square(W,L,R,x1,x2,y1,y2,lowb,upb,leftb,rightb):
    #print "Filling",x1,y1," to ",x2,y2
    #print "With", R
    if x1>x2 or y1>y2:
        return R,[]
    if len(R)==0:
        return [],[]
    circx = R[0]+x1
    circy = R[0]+y1
    rad = R[0]
    if lowb:
        circy=y1
    if leftb:
        circx = x1
    boundx = x2-R[0]
    boundy = y2 - R[0]
    if rightb:
        boundx = x2
    if upb:
        boundy = y2
        
    #print circx,circy,rad, boundx,boundy
    if boundx < circx or boundy < circy:
        #print "Can't fit"
        Left,Used = fill_square(W,L,R[1:],x1,x2,y1,y2,lowb,upb,leftb,rightb)
        return [R[0]]+Left,Used
    else:
        R = R[1:]
        #Lower box
        Left, Used = fill_square(W,L,R,min(circx +rad,W),x2,y1,y2,lowb,upb,False,rightb)
        if len(Used)==0:
            Left2, Used2 = fill_square(W,L,Left,x1,x2,min(circy+rad,L),y2,False,upb,leftb,rightb)
        else:
            Left2, Used2 = fill_square(W,L,Left,x1,min(circx+rad,W),min(circy+rad,L),y2,False,upb,leftb,False)
        return Left2, Used+Used2 +[[rad,circx,circy]]       
for t in range(1,T+1):
    N,W,L = [int(x) for x in raw_input().split()]
    R = [int(x) for x in raw_input().split()]
    R2 = [[R[x],x] for x in range(N)]
    R.sort()
    R.reverse()
    R2.sort()
    R2.reverse()
    #print R
    #print R2
    L,U = fill_square(W,L,R,0,W,0,L,True,True,True,True)
    #print L
    #print U
    if len(L)>0:
        print "PROBLEM"
    U.sort()
    U.reverse()
    xcords = [0]*N
    ycords = [0]*N
    #print U
    s = ""
    for i in range(N):
        index = R2[i][1]
        xcords[index] = U[i][1]
        ycords[index] = U[i][2]
    for i in range(N):
        s+=" "+str(xcords[i])
        s+=" "+str(ycords[i])
    print "Case #"+str(t)+":"+s
