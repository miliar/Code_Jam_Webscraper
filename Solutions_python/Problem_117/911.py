
T=int(input())

for i in range(T):
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    tab=[]
    for j in range(a):
        l=input().split()
        tab.append([])
        for ll in range(b):
            tab[j].append(int(l[ll]))
    ta=[]
    for j in range(a):
        ta.append(max(tab[j]))
    tb=[]
    for j in range(b):
        tb.append(0)
        for jj in range(a):
            tb[j]=max(tb[j],tab[jj][j])
    r="YES"
    for j in range(a):
        for x in range(b):
            if(tab[j][x]<ta[j] and tab[j][x]<tb[x]):
                r="NO"
    print("Case #"+str(i+1)+": "+str(r))
