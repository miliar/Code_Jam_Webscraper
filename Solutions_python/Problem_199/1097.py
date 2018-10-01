# Ernest van Wijland
# Python3
T=int(input())

def flip(K,pan):
    for i in range(K):
        if pan[i]=="+":
            pan[i]="-"
        else:
            pan[i]="+"
    return pan

for t in range(1,T+1):
    s,K=input().split()
    pan=[i for i in s]
    K=int(K)
    mvt=0
    while(len(pan)>=K):
        A=0
        B=0
        S=0
        i=0
        while i<len(pan) and pan[i]=="+":
            pan=pan[i+1:len(pan)]
        cnt=0
        i=0
        while i<len(pan) and pan[i]=="-":
            cnt+=1
            i+=1
        A=cnt//K
        mvt+=A
        pan=pan[A*K:len(pan)]
        if len(pan)<K:
            break
        if cnt!=K*A:
            mvt+=1
            pan=flip(K,pan)
    onlyPlus=True
    for i in pan:
        if i=="-":
            onlyPlus=False
    print("Case #",end="")
    print(t,end="")
    print(": ",end="")
    if onlyPlus:
        print(mvt)
    else:
        print("IMPOSSIBLE")






























