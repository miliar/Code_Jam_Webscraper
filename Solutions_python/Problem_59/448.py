f=open('A-large.in','r')
ff=open('outtt.txt','w')
ss=f.readline()
t=int(ss[:len(ss)-1])
for i in range(0, t):
    s=f.readline()
    s=s[:len(s)-1]
    l=s.split(' ')
    n=int(l[0])
    m=int(l[1])
    aa=set()
    aa.add('/')
    for j in range(n):
        s=f.readline()
        s=s[:len(s)-1]
        l=s.split('/')
        pp=''
        for k in range(1, len(l)):
            pp+='/'
            pp+=l[k]
            aa.add(pp)
    ans=0
    for j in range(m):
        s=f.readline()
        if s[-1]=='\n': s=s[:len(s)-1]
        l=s.split('/')
        pp=''
        ll=len(l)
        flag=0
        for k in range(1, ll):
            pp+='/'
            pp+=l[k]
            if not flag:
                if pp in aa:
                    continue
                else:
                    ans+=ll-k
                    flag=1
            if flag:
                aa.add(pp)
    ff.write('Case #%d: %d\n'%(i+1, ans))
ff.close()
f.close()


        
                
        
            
            
        
    
