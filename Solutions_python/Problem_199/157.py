def solve(f):
  s,x = f.readline().split(' ')
  x = int(x)
  s = list(s)
  i = 0
  R = 0
  while i<=len(s)-x:
    if s[i]=='-':
      for j in range(x):
        s[i+j] = '-+'[s[i+j]=='-']
      R += 1
    i += 1
  return any(x=='-' for x in s) and "IMPOSSIBLE" or R
  
f = open("a.in")
T = int(f.readline())
for t in range(T):
  print "Case #%d: %s" %(t+1,solve(f))