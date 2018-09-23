def finish(s):
    return s == "+" * len(s)


def flip(s, i, j):
    l = list(s[i:j])
    l2 = ["-" if t == "+" else "+" for t in l]
    return s[:i] + "".join(l2) + s[j:]


def solve(s, k):
    count = 0
    for i in range(len(s) - k + 1):
        if s[i] == "-":
            s = flip(s, i, i + k)
            count += 1
    if finish(s):
        return count
    else:
        return -1


t = int(raw_input())

for i in range(1, t + 1):
    s, k = raw_input().strip().split()
    k = int(k)
    result = solve(s, k)
    if result < 0:
        result = "IMPOSSIBLE"
    else:
        result = str(result)
    print("Case #%d: %s" % (i, result))
