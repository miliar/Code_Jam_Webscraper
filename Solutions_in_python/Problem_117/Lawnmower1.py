f = open('input', 'r')
t = int(f.readline())
f1 = open('output', 'w')
for tt in xrange(t):
  [n, m] = map(int, f.readline().split())
  l1m = ['1']*m
  l0m = ['0']*m
  l1n = ['1']*n
  l0n = ['0']*n
  u = []
  for i in xrange(n):
    l = f.readline().split()
    if l == l1m:
      u += l0m
    else:
      u += l
  for i in xrange(m):
    if '2' not in u[i:m*(n-1)+1+i:m]:
      u[i:m*(n-1)+1+i:m] = l0n
  if '1' in u:
    f1.write('Case #{0}: NO\n'.format(tt+1))
  else:
    f1.write('Case #{0}: YES\n'.format(tt+1))
f.close()
f1.close()

