f=open("1.txt")
lines=f.readlines()
l=[]
for i in lines[1:]:
    l.append(i.strip().split(" "))
#print(l)    

ans=[]
_c=0
for case in l:
    _c+=1
    cnt=0
    s=case[0]
    k=int(case[1])
    leng=len(s)
    c=list(s)
    for i in range(leng-k+1):
        if c[i]=="-":
            cnt+=1
            for j in range(i,i+k):
                if c[j]=="-":
                    c[j]="+"
                else:
                    c[j]="-"
    for i in c:
        if i!="+":
            cnt="IMPOSSIBLE"
    print("Case #{:}: {:}".format(_c,cnt))                
