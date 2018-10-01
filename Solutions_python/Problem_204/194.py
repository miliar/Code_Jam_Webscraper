def mxfrac(G, A):
    mx = 0
    for i in range(len(A)):
        mx = max(mx, A[i]//G[i])
    return mx

def ans(G, Q):
    total = 0
    while True:
        A = []
        if len(Q[0]) == 0:
            break
        for i in range(len(Q)):
            A.append(max(Q[i]))
            del Q[i][Q[i].index(max(Q[i]))]
        M = mxfrac(G, A)
        mastflag = 0
        for n in range(M+1, 0, -1):
            flag = 1
            for i in range(len(G)):
                a = A[i] / n
                mn = 0.9 * G[i]
                mx = 1.1 * G[i]
                if a < mn or a > mx:
                    flag = 0
                    break
            if flag == 1:
                mastflag = 1
                break
        if mastflag == 1:
            total += 1
    return total

file = open('A.in')
out = open('A.txt', 'w')

input = file.readline
print = out.write


T = int(input())
for t in range(T):
    N, P = map(int, input().split(' '))
    G = [int(n) for n in input().split(' ')]
    Q = []
    for n in range(N):
        q = [int(i) for i in input().split(' ')]
        Q.append(q)
    print(str('Case #{}: {}\n'.format(t+1, ans(G, Q))))
            
    
        
    
        
