def flip(s, p, k):
    res = ""
    for i in xrange(len(s)):
        if i < p or i >= p + k:
            res = res + s[i]
        else:
            res = res + ('-' if s[i] == '+' else '+')
    return res

tests = int(raw_input())
for test in xrange(tests):
    s, n = raw_input().split()
    n = int(n)
    res = 0
    for i in xrange(len(s)):
        if s[i] == '-' and i + n <= len(s):
            res += 1
            s = flip(s, i, n)
    print 'Case #{}:'.format(test+1), 'IMPOSSIBLE' if '-' in s else res
