def solve(n, k):
    #print(n,k)
    d = 0
    while k > 2**d:
        n -= 2**d
        k -= 2**d
        d += 1
    #print(n,k)
    s = n // (2**d)
    if k <= n % (2**d):
        s += 1
    if s%2 == 0:
        return s//2, s//2-1
    else:
        return s//2, s//2

for case in range(1, int(input())+1):
    N, K = input().split()
    M, m = solve(int(N), int(K))
    print('Case #{}: {} {}'.format(case, M, m))
