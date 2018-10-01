def solve(N,pd,pg):
    if pg==100 or pg==0:
        if pd==pg:
            return True
        else:
            return False
    if N>=100:
        return True
    for d in range(1,N+1):
        if d*pd % 100 == 0:
            return True
    return False
    
fi = open("input.txt")
T = int(fi.readline())
for test in range(T):
    N,pd,pg = map(int,fi.readline().split())
    print "Case #"+str(test+1)+":",
    if solve(N,pd,pg):
        print "Possible"
    else:
        print "Broken"
