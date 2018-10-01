def tidy(n,ca):
    a=[]
    for i in str(n):
        a.append(int(i))
    b=sorted(a)
    if(a==b):
        print("Case #%d:"%(ca),n)
    else:
        tidy(n-1,ca)

n=input()
fp=open(n,'r')
ca=-1
for i in fp.readlines():
    ca+=1
    if(ca>0):
        tidy(int(i),ca)
