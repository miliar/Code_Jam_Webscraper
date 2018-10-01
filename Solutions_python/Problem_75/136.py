import sys

f=open(sys.argv[1])

a=f.readlines()

n=int(a[0])


for i in range(1,n+1):
    s=a[i].split()
    x=int(s[0])
    l1=s[1:1+x]
    y=int(s[1+x])
    l2=s[1+x+1:1+x+1+y]
    ans=""
    for j in s[-1]:
        ans=ans+j
        if len(ans)>1 :
            for r in l1:
                if (ans[-1]==r[0] and ans[-2]==r[1]):
                    ans=ans[0:-2]+r[2]
                if (ans[-1]==r[1] and ans[-2]==r[0]):
                    ans=ans[0:-2]+r[2]
        if len(ans)>1:
            for r in ans[0:-1]:
                if (r+ans[-1]) in l2:
                    ans=""
                    break;
                if (ans[-1]+r) in l2:
                    ans=""
                    break;
                
    ss="["
    for j in ans[0:-1]:
        ss+=j+', '
    if len(ans) > 0:
        ss+=ans[-1]
    print "Case #"+str(i)+": "+ss+"]"

