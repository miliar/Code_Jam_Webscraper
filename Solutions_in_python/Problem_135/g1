import sys
T=int(sys.stdin.readline())
for a in range(T):
    A1=int(sys.stdin.readline())
    i=1
    while i<5:
        if i==A1:
            main=[int(x) for x in sys.stdin.readline().split()]
        else:
            raw=[int(x) for x in sys.stdin.readline().split()]
        i+=1
    A2=int(sys.stdin.readline())
    i=1
    while i<5:
        if i==A2:
            slave=[int(x) for x in sys.stdin.readline().split()]
        else:
            raw=[int(x) for x in sys.stdin.readline().split()]
        i+=1
    count=0
    for c in main:
        if c in slave:
            count+=1
            ans=c
    if count==1:
        print "Case #" + str(a+1) + ": " + str(ans)
    elif count>1:
        print "Case #" + str(a+1) + ": " + "Bad magician!"
    else:
        print "Case #" + str(a+1) + ": " + "Volunteer cheated!"
        
        
