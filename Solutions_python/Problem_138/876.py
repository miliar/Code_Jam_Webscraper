fh=open('js-large4.in','r')
gh=open('js-large4.out','w')
T=int(fh.readline())
for num in range(1,51):
    s='Case #'+str(num)+': '
    N=int(fh.readline())
    lst=fh.readline().split()
    lstN=list(map(float,lst))
    lstN.sort()
    lst1=fh.readline().split()
    lstK=list(map(float,lst1))
    lstK.sort()
    for i in range(0,N):
        found=1
        for j in range(i,N):
            if lstN[j]<lstK[j-i]:
                found=0
                break
        if found==1:
            break
    if found==1: 
        deceit=N-i
    else: 
        deceit=0
    k=0
    for i in range(0,N):
        found=0
        for j in range(k,N):
            if lstK[j]>lstN[i]:
                found=1
                k=j+1
                break
        if found==0:
            war=N-i
            break;
    if found==1:
        war=0
    gh.write(s+str(deceit)+' '+str(war)+'\n')
fh.close()
gh.close()