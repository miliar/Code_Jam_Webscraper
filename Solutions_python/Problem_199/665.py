T = int(raw_input())

for t in range (0, T):
    b = raw_input().split(" ")
    a = []
    s = []
    n = len(b[0])
    k = int(b[1])
    a.append(0)
    s.append(0)
    s.append(0)
    for i in range(n):
        if b[0][i] == '+':
            a.append(0)
        else:
            a.append(1)
        s.append(0)
    res = 0
    possible = True
    for i in range(1, n + 1):
        s[i] = s[i] + s[i - 1]
        a[i] = a[i] + s[i]
        if a[i] % 2 == 1:
            if i <= n - k + 1:
                res += 1
                s[i] += 1
                s[i + k] -= 1
            else:
                possible = False
    if possible:
        print "Case #" + str(t + 1) + ": " + str(res)
    else:
        print "Case #" + str(t + 1) + ": IMPOSSIBLE"
