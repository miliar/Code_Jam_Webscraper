import sys
# parse command line
if len(sys.argv) > 1:
    inf = open(sys.argv[1])
else:
    inf = open('a.in')


T = int(inf.readline())

for x in range(1,T+1):
    N = int(inf.readline())
    m = map(int, inf.readline().split(' '))

    a, b = 0, 0

    if N > 1:
        maxdif = 0
        for i in range(1, N):
            dif = m[i-1] - m[i]
            if dif > 0: a+=dif
            
            if dif > maxdif:
                maxdif = dif

        tasa = maxdif
        for i in range(N - 1):
            b += min(tasa, m[i])

    print 'Case #%d: %d %d' % (x, a, b)
