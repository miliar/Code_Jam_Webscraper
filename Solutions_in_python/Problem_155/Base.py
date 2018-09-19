import sys

args = sys.argv
file = args[1]
f = open(file)

cases = int(f.readline())

for i in range(cases):
    l = f.readline().split(' ')
    n = int(l[0])
    a0 = [int(y) for y in l[1][:-1]]
    a = range(n + 1)
    for j in range (n):
        a[j + 1] = a[j] + a0[j]
    b = range(n + 1)
    c = map(lambda (x,y) : x - y,zip(b,a))
    d = max(c)
    print "Case #%s: %s" % (i + 1, d)
    
