import sys
f = sys.stdin
if len(sys.argv)>=2:
    fn=sys.argv[1]
    if fn!='_':
        f=open(fn)
output=open('output.out','w')
t=int(f.readline())
for test in xrange(1,t+1):
    cout=0
    str1="Case #%d: "%(test)
    output.write(str1)
    qad=map(int,f.readline().strip().split())
    n=qad[0]
    s=qad[1]
    p=qad[2]
    nk=qad[3:]
    nk.sort()
    g1=0
    x=0
    for i in nk:
        temp=i-p
        temp/=2
        if g1==1 and i>=x:
            cout+=1
        elif temp>=p-1 and temp>=0:
            cout+=1
            g1=1
            x=i
        elif temp>=p-2 and s>=1 and temp>=0:
                cout+=1
                s-=1
    output.write(str(cout)+"\n")
output.close()
        
