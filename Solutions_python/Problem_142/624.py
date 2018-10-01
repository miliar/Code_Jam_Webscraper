
f = open(r"e:\downloads\a-small-attempt0.in", "r")
#f = open(r"e:\downloads\the_repeater.txt", "r")

def char_count(s):
    res = []
    i = 0
    while i < len(s):
        c = s[i]
        j = i+1
        while j < len(s) and s[j] == c:
            j += 1
        res.append((c, j-i))
        i = j

    return res

def stem(a):
    r = ''
    for c, i in a:
        r += c
    return r


def min_cost(u):
    u.sort()
    r = 0
    for i in range(1, len(u)):
        r += abs(u[i]-u[i-1])

    return r

def min_ops(a):
    a = [char_count(s) for s in a]
    s = set([stem(x) for x in a])
    if len(s) > 1:
        return -1
    else:
        res = 0
        n = len(a[0])
        for i in range(n):
            u = []
            for v in a:
                u.append(v[i][1])
            res += min_cost(u)

        return res



T = int(f.readline())
for t in range(1, T+1):
    N  = int(f.readline())
    a = []
    for _ in range(N):
        a.append(f.readline().strip())


    res = min_ops(a)
    if res == -1:
        print("Case #%d: Fegla Won" % t)
    else:
        print("Case #%d: %d" % (t, res))
