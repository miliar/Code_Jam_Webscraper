T = int(raw_input())
for C in xrange(T):
    n, x = map(int, raw_input().strip().split())
    files = sorted(map(int, raw_input().strip().split()))
    lo, hi = 0, len(files)-1
    ans = 0
    while lo < hi:
        if files[lo] + files[hi] <= x:
            lo += 1
        hi -= 1
        ans += 1
    if lo == hi: ans += 1
    print "Case #" + str(C+1) + ": " + str(ans)
