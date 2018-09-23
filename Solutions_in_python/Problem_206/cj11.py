for i in range(input()):
    d,n = map(int, raw_input().split())
    a=0
    for j in range(n):
        k,s = map(int, raw_input().split())
        if k<d:
            t = (d-k)*1.0/s
            a = max(a, t)
    print "Case #" + str(i+1) + ": " + '{0:.8f}'.format(d/a)

