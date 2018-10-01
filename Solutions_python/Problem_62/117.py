T = input()
for case in range(1, T + 1):
    N = input()
    A, B = {}, {}
    for i in range(N):
        a, b = map(int, raw_input().split())
        A[a] = i
        B[b] = i
    ans = 0
    for x in sorted(A):
        s = 0
        for y in sorted(B):
            if B[y] == A[x]:
                A.pop(x)
                B.pop(y)
                ans += s
                break
            s += 1
    print 'Case #%s: %s' % (case, ans)

