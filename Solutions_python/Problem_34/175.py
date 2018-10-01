import re;
f=open('in.txt');
o=open('out.txt','w');
(L,D,N)=(int(t) for t in f.readline().split());
txt=[];
for i in range(D):
    txt.append(f.readline());

for i in range(N):
    p=f.readline();
    p=p.replace('(','[').replace(')',']');
    n=0;
    for t in txt:
        if re.match(p,t)!=None:
            n+=1;
    o.write(str.format('Case #{}: {}\n',i+1,n));

o.close();
f.close();
