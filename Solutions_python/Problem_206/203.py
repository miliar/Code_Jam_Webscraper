T = int(input())

for t in range(1,T+1):
    D , N = [int(c) for c in input().split(' ')]

    time = 0
    
    for i in range(N):
        K, S = [int(c) for c in input().split(' ')]
        T = (D-K)/S
        if T > time:
            time = T

    V = D/time
            
    print('Case #{}: {:.6f}'.format(t,V))

