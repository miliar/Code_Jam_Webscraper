from sys import stdin, stdout

T = int(stdin.readline().strip())
for i in range(T):
    N = int(stdin.readline().strip())
    P = []
    for j in range(N):
        row = stdin.readline().strip()
        p = row.rfind('1')
        P.append(p)
    K = 0
    for j in range(N):
        for k in range(j, N):
            if P[k] <= j:
                break
        if k != j:
            K += k - j
            P = P[:j] + [P[k]] + P[j:k] + P[k + 1:]
    stdout.write('Case #%d: %d\n' % (i + 1, K))
