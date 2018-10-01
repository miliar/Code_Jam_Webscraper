cnt = int(input())
for i in range(1, 1+cnt):
    N, M = input().split(' ')
    N, M = int(N), int(M)
    R, C = N*[False], N*[False]
    S, D = set(), set()
    V = [N*['.'] for i in range(N)]
    scr=0
    for j in range(M):
        T, X, Y = input().split(' ')
        X, Y = int(X)-1, int(Y)-1
        V[X][Y]=T
        if T == 'x' or T == 'o':
            R[Y] = True
            C[X] = True
            scr+=1
        if T == '+' or T == 'o':
            S = S | {X+Y}
            D = D | {X-Y}
            scr+=1
    lns = set()
    for X in range(N):
        if not C[X]:
            Y = [Y for Y in range(N) if not R[Y]][0]
            T = 'x'
            if V[X][Y] == '+':
                T='o'
            V[X][Y] = T
            C[X] = True
            R[Y] = True
            scr+=1
            lns = lns | {X+Y*N}
    B = [(0, 0), (N-1, 0), (N-1, N-1), (0, N-1)]
    C = [[(1, 0),(0, 1)], [(0, 1),(-1, 0)], [(-1, 0),(0, -1)], [(0, -1),(1, 0)]]
    for M in range((N//2)+1):
        for J in range((N//2)+1-M):
            for I in range(4):
                for K in range(2):
                    X, Y = B[I]
                    X += (J+M)*C[I][K][0]+M*C[I][1-K][0]
                    Y += (J+M)*C[I][K][1]+M*C[I][1-K][1]
                    if (not (X+Y) in S) and (not (X-Y) in D):
                        T = '+'
                        if V[X][Y] == 'x':
                            T='o'
                        V[X][Y] = T
                        S = S | {X+Y}
                        D = D | {X-Y}
                        scr+=1
                        lns = lns | {X+Y*N}
    print('Case #'+str(i)+ ': '+str(scr)+' '+str(len(lns)))
    for l in lns:
        print(V[l%N][l//N] + ' ' + str(l%N+1) + ' ' + str(l//N+1))
        