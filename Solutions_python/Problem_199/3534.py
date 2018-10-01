def solve(s, k):
    n, i, count = len(s), 0, 0
    while i < n:
        if s[i] == "-":
            if i + k > n: return "IMPOSSIBLE"
            for j in range(i, i + k): s[j] = ("+" if s[j] == "-" else "-")
            count += 1
        i += 1
    return str(count)

t = int(raw_input().strip())
for _ in range(1, t + 1):
    s, k = raw_input().split()
    print "Case #" + str(_) + ":", solve(list(s), int(k))