#Python 2

T=int(raw_input())
x=1
while x<=T:
    N=int(raw_input())
    Ci=[int(a) for a in raw_input().split()]
    S=0
    for a in Ci:
        S=S^a
    if(S==0):
        Bpile=sum(Ci)-min(Ci)
        print "Case #%d: %d" % (x, Bpile)
    else:
        print "Case #%d: NO" % (x,)
    x=x+1
