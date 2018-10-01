def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

c = int(raw_input())



for ci in range(1,c+1):
   e = [int(i) for i in raw_input().split(' ')]
   print "Case #%d:"%ci,
   n = e[0]
   e = e[1:]
   e.sort()
   d = []
   for j in range(1, n):
       d.append(e[j]-e[j-1])
   r = d[0]
   for j in range(1, n-1):
       r = gcd(r, d[j])
   if e[0]%r:
       print r-(e[0]%r)
   else:
       print 0
