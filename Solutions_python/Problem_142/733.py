def similarity(a,b):
    i=0
    j=0
    diff=0
    while i<len(a):
        letter=a[i]
        counta=0
        while i<len(a) and a[i]==letter:
            counta+=1
            i+=1
        countb=0
        while j<len(b) and b[j]==letter:
            countb+=1
            j+=1
        if countb==0:
            return 'Fegla Won'
        diff+=abs(counta-countb)
    return diff
                    
f=open('A-small-attempt4.in')
g=open('result.in','w')
T=int(f.readline())
for case in range(1,T+1):
    N=int(f.readline())
    s=[]
    for i in range(N):
        s.append(f.readline())
    r=similarity(s[0],s[1])
    print r
    g.write('Case #'+str(case)+': '+str(r)+'\n')
g.close()
f.close()
    
    
