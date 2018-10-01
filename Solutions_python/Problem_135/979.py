tc=int(input("TC"))
a=[]
for t in range(tc):
    r=int(input())-1
    mat=[]
    for i in range(4):
        mat.append(input())
        mat[i]=[j for j in mat[i].split(" ")]
    save1=mat[r]
    r=int(input())-1
    mat=[]
    for i in range(4):
        mat.append(input())
        mat[i]=[j for j in mat[i].split(" ")]
    ans=[]
    save2=mat[r]
    for i in save1:
        for j in save2:
            if i==j:
                ans+=[i]
    if len(ans)==1:
        a+=ans
    elif len(ans)>1:
        a+=['Bad magician!']
    else:
        a+=['Volunteer cheated!']
for i in range(len(a)):
    print("Case #"+str(i+1)+": "+a[i])
        
