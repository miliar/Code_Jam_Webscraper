t = int(raw_input())
for i in range(t):
    l = raw_input().split()
    n, a = int(l[0]), l[1]
    s, c = 0, 0
    for j in range(n+1):
        if s < j:
            c += (j-s)
            s += (j-s)
        s += int(a[j])
    print 'Case #{0}: {1}'.format(i+1, c)