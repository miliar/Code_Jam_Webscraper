t, T = 0, int(input())
while t != T:
    t += 1

    A, B = map(int, input().split())
    P = tuple(map(float, input().split()))

    best = 2+B # option 3

    for backspace in range(0,A+1):
        current = backspace + 1 # plus enter
        current += B - (A-backspace)
        
        right = current
        wrong = current + B + 1
        
        pright = 1
        for i in range(0, A-backspace):
            pright *= P[i]
        pwrong = 1-pright

        best = min(best,pright*right+pwrong*wrong)

    print("Case #%d: %.6f" % (t, best))
            
