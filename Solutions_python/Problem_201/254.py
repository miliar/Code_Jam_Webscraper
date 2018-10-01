from sys import stdin

t  = int(stdin.readline())
for ca in xrange(1,t+1):
 n,k = map(int,stdin.readline().split())
 i = 0
 req = k
 while True:
  if 2**i >=req:
   break
  req -= 2**i
  i+=1
 num = n
 ans = 0
 s = []
 if req:
  req-=1
  for j in xrange(i):
   if req & (1<<j):
    s.append('R')
   else:
    s.append('L')
 for i in s:
  if i=='L':
   num = num/2
  else:
   num = (num-1)/2
 print "Case #%d: %d %d"%(ca,num/2, (num-1)/2)
