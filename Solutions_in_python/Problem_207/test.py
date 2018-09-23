T=int(input())
for t in range(1,T+1):
    print("Case #",end="")
    print(t,end=": ")
    N,R,O,Y,G,B,V=map(int,input().split())
    l=[(R,"R"),(Y,"Y"),(B,"B")]
    if(max(l)[0]>float(N/2)):
        print("IMPOSSIBLE")
        continue
    if(l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[0][0]==N/3):
        for i in range(int(N/3)):
            print("RYB",end="")
        print("")
        continue
    s="";
    l.sort()
    R=l[2][0]
    r=l[2][1]
    Y=l[1][0]
    y=l[1][1]
    B=l[0][0]
    b=l[0][1]
    for i in range(R): s+=r
    idx=0
    for i in range(Y):
        s=s[0:idx]+y+s[idx:len(s)]
        idx+=2
    left=1
    for i in range(B):
        s=s[0:len(s)-left]+b+s[len(s)-left:len(s)]
        left+=2
    print(s)
