def solve():
    N, X = map(int, raw_input().split())
    S = map(int, raw_input().split())
    S.sort()
    count = 0
    i = 0
    j = len(S) - 1
    while i <= j:
        if S[i] + S[j] <= X:
            i += 1
            j -= 1
            count += 1
        elif S[j] <= X:
            j -= 1
            count += 1
    return count

T = int(raw_input())
for i in range(T):
    print 'Case #%d:' % (i + 1), solve()
