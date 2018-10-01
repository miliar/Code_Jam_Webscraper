def f(X,S,R,t,W):
    A=[]
    for B,E,w in W:
        D=E-B
        A.append((D,w+S))
        X-=D
    if X!=0:
        A.append((X,S))
    A=list(sorted(A,key=lambda x:x[1]))
##    print(A,R-S,t)
    re=0
    for d,s in A:
        if t!=0:
            if (R-S+s)*t<=d:
                re+=t+(d-(R-S+s)*t)/s
                t=0
            else:
                time=d/(R-S+s)
                re+=time
                t-=time
        else:
            re+=d/s
    return re
def main():
    with open('A-large.in') as fin,\
         open('A-large.out','w') as fout:
        rint=lambda f:int(next(f))
        rints=lambda f:list(map(int,next(f).strip().split()))
        for i in range(rint(fin)):
            X,S,R,t,N=rints(fin)
            W=[rints(fin) for j in range(N)]
            re=f(X,S,R,t,W)
            print(str.format("Case #{0}: {1}",i+1,re))
            print(str.format("Case #{0}: {1}",i+1,re),file=fout)
main()
