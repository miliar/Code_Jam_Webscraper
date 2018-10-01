fi=open('C-small-attempt0.in','r')
z=fi.readlines()
fi.close()
t=int(z[0])
f=open('out.txt','w')
for i in range(t):
    f.write('Case #%d: '%(i+1))
    a=int(z[i+1].split()[0])
    b=int(z[i+1].split()[1])
    tt=[]
    cnt=0
    #print '======='
    for j in range(b,a-1,-1):
        if j<10:
            break
        if j not in tt:
            s=str(j)
            l=len(s)
            tmp=1
            tt.append(j)
            for k in range(l-1):
                s=s[1:]+s[0]
                p=int(s)
                if a<=p<=b and not p in tt:
                    tmp+=1
                    tt.append(p)
            #if tmp>1:
            #    print str(j)
            cnt+=tmp*(tmp-1)/2
    f.write('%d\n'%cnt)
f.close()
