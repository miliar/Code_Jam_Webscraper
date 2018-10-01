def tidy(n):
    s = str(n)
    for i in range(1, len(s)):
        if int(s[i]) < int(s[i-1]):
            return False
    return True

assert tidy(123)
assert tidy(999999999)
assert not tidy(20)

def solve(n):
    for i in range(n, 0, -1):
        if tidy(i):
            return i
    return 1


t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    ans = solve(n)
    print "Case #{}: {}".format(i, ans)