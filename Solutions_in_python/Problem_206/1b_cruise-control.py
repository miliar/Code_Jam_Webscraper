T = int(input())
for z in range(T):
    IN = input().split(' ')
    D = int(IN[0])
    N = int(IN[1])
    maxTime = 0
    minSpeed = 0
    displacement = D
    for i in range(N):
        SN = input().split(' ')
        S = int(SN[0])
        V = int(SN[1])
        timeRequired = (D-S)/V
        if(timeRequired>=maxTime):
            minSpeed = V
            maxTime = timeRequired
            displacement = S
    Vr = minSpeed + displacement/maxTime
    if(z == T-1):
        print("Case #"+str(T)+": "+str(Vr),end='')
    else:
        print("Case #"+str(z+1)+": "+ str(Vr))
