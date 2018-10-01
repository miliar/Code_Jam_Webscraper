def ints():
    return map(int, raw_input().split())

num_cases, = ints()

for case_num in xrange(1, num_cases + 1):
    N, X = ints()
    S = ints()
    S.sort()
    ans = 0
    i = 0
    j = N-1
    while i < j:
        ans += 1
        if S[i] + S[j] <= X:
            i += 1
            j -= 1
        else:
            j -= 1
    if i == j:
        ans += 1
    print "Case #%d: %s" % (case_num, ans)
