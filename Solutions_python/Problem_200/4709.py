def cal(t):
    a = str(t)
    l = len(a)
    i = 0
    while (i < l - 1):
        if (a[i] <= a[i + 1]):
            i += 1
            continue
        else:
            return 0
    return t


def tidy(a):
    b = cal(a)
    while (b == 0):
        a -= 1
        b = cal(a)
    return b


r = []
out = open('B-small-attempt1.out', 'w')
for line in open('B-small-attempt1.in', 'r'):
    r.append(line.rstrip())
for i in range(1, int(r[0]) + 1):
    n = tidy(int(r[i]))
    out.write("Case #{}: {}\n".format(i, n))
out.close()
