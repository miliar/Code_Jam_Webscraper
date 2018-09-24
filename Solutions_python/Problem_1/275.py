f=open("A-large.in")
w=open("a.txt",'w')
s=f.read().split('\n')
n=int(s.pop(0))
for k in range(n):
    i=int(s.pop(0))
    d=dict()
    switch=0
    unused=i
    for c in range(i):
        d[s.pop(0)]=1
    q=int(s.pop(0))
    for c in range(q):
        unused-=d[s[0]]
        d[s[0]]=0
        if unused==0:
            switch+=1
            for j in d.keys():
                d[j]=1
            d[s[0]]=0
            unused=i-1
        s.pop(0)
    w.write("Case #"+str(k+1)+": "+str(switch)+'\n')
f.close()
w.close()
                
