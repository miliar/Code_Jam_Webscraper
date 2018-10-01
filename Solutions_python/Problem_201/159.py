def solve(f):
  N,k = map(int,f.readline().split(' '))
  A = {N:1}
  I = [N]
  while 1:
    i = I.pop(0)
    a = A[i]
    s = (i-1)/2
    b = i-s-1
    if a>=k:
      return "%d %d" %(b,s)
    if b in A:
      A[b] += a
    else:
      A[b] = a
      I += [b]
    if s in A:
      A[s] += a
    else:
      A[s] = a
      I += [s]
    k -= a
  return 0
  
def out(s):
  print s
  o.write(s)
  
f = open("i.in")
o = open("o.out", "wt")
T = int(f.readline())
for t in range(T):
  out("Case #%d: %s" %(t+1,solve(f)))
  o.write('\n')
o.close()