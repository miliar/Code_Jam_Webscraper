T=int(input())

def tidy(N):
    l=[]
    m=[]
    N=str(N)
    for i in range(len(N)):
        l.append(int(N[i]))
        m.append(int(N[i]))
    l.reverse()
    m.reverse()
    for i in range(1,len(l)):
        if(l[i]>l[i-1]):
            l[i]-=1
            for j in range(i-1,-1,-1):
                l[j]=9
    zero=False
    for j in reversed(l):
        if(j!=0):
            zero=True
        if(j==0 and zero==False):
            continue
        print(j,end="")
    print()

for t in range(1,T+1):  
    N=int(input())
    print("Case #",end="")
    print(t,end="")
    print(": ",end="")
    tidy(N)
