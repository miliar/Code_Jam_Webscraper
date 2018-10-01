T = int(raw_input())

str = 'welcome to code jam'
N = len(str)


def conta(i=0, j=0):
    if i == N:
        return 1
    if j == M:
        return 0
    if not (i, j) in memo:
        resp = 0
        for k in range(j, M):
            if linha[k] == str[i]:
                resp = (resp + conta(i+1, k+1)) % 10000
        memo[(i, j)] = resp
    return memo[(i, j)]

for t in range(T):
    memo = {}
    linha = raw_input().strip()
    M = len(linha)

    print 'Case #%d: %04d' % (t+1, conta())


