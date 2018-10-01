def flip(seq, start, n):
    for i in range(start, start+n):
        if seq[i] == 0:
            seq[i] = 1
        else:
            seq[i] = 0

t = int(input())
for a0 in range(t):
    s, n = input().split(' ')
    n = int(n)
    s = [1 if c == "+" else 0 for c in s]
    res = 0
    for p in range(len(s)-n+1):
        if s[p] == 0:
            flip(s, p, n)
            res += 1
    failed = False
    for x in range(len(s)-n+1, len(s)):
        if s[x] == 0:
            failed = True
    if failed:
        print("Case #" + str(a0+1) + ": " + "IMPOSSIBLE")
    else:
        print("Case #" + str(a0+1) + ": " + str(res))
