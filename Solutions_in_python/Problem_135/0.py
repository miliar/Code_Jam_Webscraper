fh=open('js-small1.in','r')
gh=open('js-small1.out','w')
T=int(fh.readline())
for num in range(1,101):
    s='Case #'+str(num)+': '
    m=int(fh.readline())
    for row in range(4):
       lst=fh.readline().split()
       if row==(m-1):
            lst1=list(map(int,lst))
    n=int(fh.readline())
    for row in range(4):
        lst2=fh.readline().split()
        if row==(n-1):
            lst3=list(map(int,lst2))
    count=0
    for i in range(4):
        k=lst1[i]
        for j in range(4):
            if k==lst3[j]:
                count+=1
                ans=k
    if count==0:
        gh.write(s+'Volunteer cheated!'+'\n')
    elif count>1:
        gh.write(s+'Bad magician!'+'\n')
    else:
        gh.write(s+str(ans)+'\n')
fh.close()
gh.close()