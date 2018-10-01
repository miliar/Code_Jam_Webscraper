import sys
f = sys.stdin
if len(sys.argv)>=2:
    fn=sys.argv[1]
    if fn!='_':
        f=open(fn)
output=open('revout.out','w')
t=int(f.readline())
for test in xrange(1,t+1):
    cout=0
    str1="Case #%d: "%(test)
    output.write(str1)
    a=map(int,f.readline().strip().split())
    s=a[0]
    t=a[1]
    u=a[2]
    g=a[3:]
    g.sort()
    g1=0
    x=0
    for i in g:
        temp=i-u
        temp/=2
        if g1==1 and i>=x:
            cout+=1
        elif temp>=u-1 and temp>=0:
            cout+=1
            g1=1
            x=i
        elif temp>=u-2 and t>=1 and temp>=0:
                cout+=1
                t-=1
    output.write(str(cout)+"\n")
output.close()
        
