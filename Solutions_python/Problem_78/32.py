import fractions
T=int(input())
for i in range(T):
  N,pd,pg=[int(x) for x in input().split()]
  ming = 100//(fractions.gcd(100,pd))
  dposs = bool(ming<=N)
  gposs = (0<pg<100) or (pd==pg)
  ans = 'Possible' if (dposs and gposs) else 'Broken'
  print('Case #%d: ' % (i+1),ans,sep='')