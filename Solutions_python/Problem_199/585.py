
def solve():
  p,k = raw_input().split()
  k = int(k)
  n = len(p)
  ans = 0
  p = map(lambda x:0 if x=='-' else 1, p)
  for i in xrange(n):
    if(p[i] == 0 and i+k <= n):
      ans += 1
      for j in xrange(k):
        p[i+j] = 1 - p[i+j]
    #~ print p
  
  if sum(p)!=n:
    print 'IMPOSSIBLE'
  else:
    print ans

a = int(raw_input())

for x in xrange(a):
  print 'Case #%d:'%(x+1),
  solve()
