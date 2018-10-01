def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

fin = open('B-large.in','r')
fout = open('B.out','w')

Tn = int(fin.readline())
for T in range(Tn):
    data = [int(x) for x in fin.readline().split()]
    n = data[0]
    data.pop(0)
    data.sort()

#    print data
    g = data[1]-data[0]
#    print g
    for i in range(n):
        for j in range(i+1,n):
            g = gcd(g, data[j]-data[i])
#            print data[j]-data[i], g

#    print g
    ans = data[0] % g
    if ans > 0: ans = g - ans
    print >>fout, 'Case #%d: %d' % (T + 1, ans)
fin.close()
fout.close()