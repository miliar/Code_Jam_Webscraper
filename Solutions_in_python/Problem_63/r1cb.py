import sys

def dbg(obj):
    print>>sys.stderr,obj

f = open('B-large.in')
cases_num = int(f.readline().strip())
for case in range(cases_num):
    print 'Case #%d:'%(case+1),
    L,P,C=[int(s) for s in f.readline().split()]
    p=P
    cc=1
    #pl=[]
    while p>L:
        #pl.append(p)
        cc+=1
        if p%C<>0: p+=C-p%C
        p/=C
    #dbg(cc)
    #pl.append(L)
    #dbg(pl)
    rs=0
    while cc>2:
        cc=cc/2+1
        #dbg(cc)
        rs+=1
    print rs
f.close()    