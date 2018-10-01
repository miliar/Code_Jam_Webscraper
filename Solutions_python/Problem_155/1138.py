import sys
filename='A-large.in'
f=open(filename,"r")
f2=open("result_"+filename,"w")
tmp=sys.stdout
sys.stdout=f2

t=f.readlines()
#print t
for i in xrange(1,int(t[0])+1) :
    d={}
    cur=0
    curi=0
    ans=0
    x,y,=t[i].split();
    for j in xrange(len(y)) :
        d[j]=int(y[j])
    x=int(x)
    while cur < x :
        if curi<=(cur) : 
            cur+=d[curi]
            curi+=1
        else :
            ans+=1
            cur+=1

    print "Case #%d: %d" %(i,ans)
sys.stdout=tmp
print "finish"
