def f(s, k):
    l = []
    for i in s:
        if i == '-':
            l.append(0)
        else:
            l.append(1)
    count = 0
    for i in range(len(s) - k + 1):
        if l[i] == 0:
            count += 1
            for j in range(i, i + k):
                l[j] = 1 - l[j]
    for i in range(len(s) - k + 1, len(s)):
        if l[i] == 0:
            return "IMPOSSIBLE"
    return count

T = int(input())
for case in range(1, T+1):
    a,b = input().split()
    ans = f(a, int(b))
    print("Case #%s: %s" % (case, ans))

