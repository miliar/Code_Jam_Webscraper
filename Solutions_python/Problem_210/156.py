input = open('task2.in', 'r')
output = open('output.txt', 'w+')
T = int(input.readline())

for t in range(T):
    points = []
    N, K = map(int, input.readline().split())
    R = [(0, 0) for i in range(N)]
    S = [(0, 0) for i in range(K)]
    for i in range(N):
        x, y = map(int, input.readline().split())
        R[i] = (x, y)
    for i in range(K):
        x, y = map(int, input.readline().split())
        S[i] = (x, y)
    R = sorted(R)
    S = sorted(S)
    if N < 2 and K < 2:
        rez = 2
    if N == 2:
        if R[0][0] + 720 < R[1][1] and R[1][0] - R[0][1] < 720:
            rez = 4
        else:
            rez = 2
    if K == 2:
        if S[0][0] + 720 < S[1][1] and S[1][0] - S[0][1] < 720:
            rez = 4
        else:
            rez = 2
    output.write("Case #{}: {}\n".format(t + 1, rez))