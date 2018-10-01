casen=input()
x=[]
y=[]

for i in range(casen):
    check=0
    x=[int(s) for s in raw_input().split()]
    N,M,A=x[0],x[1],x[2]
    for x1 in range(N+1):
        if check==1:
            break;
        for y1 in range(M+1):
            if check==1:
                break
            for x2 in range(N+1):
                if check==1:
                    break
                for y2 in range(M+1):
                    if abs(x1*y2-x2*y1)==A:
                        print "Case #%d: 0 0 %d %d %d %d" %(i+1, x1, y1, x2, y2)
                        check=1
                        break
                        
    else:
        print "Case #%d: IMPOSSIBLE" %(i+1)
