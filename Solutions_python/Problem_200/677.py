T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    r = 0
    c = 1
    while N/c:
        if (N/c)%10 < N/(c*10)%10:
            N = 10*c*(N/(10*c))-1
        c*=10
    print 'Case #'+str(i+1)+':'+' '+str(N)