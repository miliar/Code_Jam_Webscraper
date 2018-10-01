t= int(input())
for i in range(1, t+1):
  D, N= map(int, input().split())
  m= 0
  for _ in range(N):
    di, si= map(int, input().split())
    tt= (D-di)/si
    m= max(m, tt)
  ans= D/m
  print('CASE #{0}: {1:.6f}'.format(i, ans))