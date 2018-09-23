from math import pi

T = int(input())
for t in range(T):
  n, k = map(int, input().split())
  data = [list(map(int, input().split())) for n in range(n)]
  data.sort(key = lambda x: x[0]*x[1], reverse = True)
  m1 = max(data[:k], key = lambda x: x[0]*x[0])
  v1 = m1[0]*m1[0] + 2*sum([x[0]*x[1] for x in data[:k]])
  m2 = max(data, key = lambda x: (x[0]*x[0], x[1]))
  data.remove(m2)
  data.insert(0, m2)
  v2 = m2[0]*m2[0] + 2*sum([x[0]*x[1] for x in data[:k]])
  res = max(v1, v2)*pi
  print("Case #"+str(t+1)+":", res)
  