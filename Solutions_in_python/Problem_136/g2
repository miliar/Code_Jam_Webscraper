import sys
T=int(sys.stdin.readline())
for a in range(T):
    C,F,X=[float(x) for x in sys.stdin.readline().split()]
    S=0
    CR=2
    time=float(X)/CR
    while True:
        S=S+float(C)/CR
        CR=CR+F
        if S>time:   
            break
        m=float(X)/CR + S
        if time>m:
            time=m
    print "Case #" + str(a+1)+ ": " + str("{0:.7f}".format(time))
            
            
            
    
