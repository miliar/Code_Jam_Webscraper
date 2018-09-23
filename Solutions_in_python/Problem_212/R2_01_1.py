T = int(input())

for ijk in range(1,T+1):
  N, P = map(int, input().split())
  G = list(map(int, input().split()))
  d = dict()
  for i in range(P):
    d[i] = 0
  for i in G:
    j = i%P
    d[j] += 1
  ret = 0
  if P == 2:
    ret = d[0] + d[1]//2
    if d[1]%2 == 1:
      ret += 1
  elif P == 3:
    ret = d[0] + min(d[1],d[2])
    if d[1] > d[2]:
      d[1] = d[1]-d[2]
      ret += (d[1]+2)//3
    elif d[2] > d[1]:
      d[2] = d[2]-d[1]
      ret += (d[2]+2)//3
  elif P == 4:
    ret = d[0] + min(d[1],d[3])
    if d[1] > d[3]:
      d[1] = d[1] - d[3]
      d[3] = 0
      ret += min(d[1]//2,d[2])
      if d[1] >= 2*d[2]:
        d[1] -= 2*d[2]
        ret += (d[1] + 3)//4
      else:
        d[2] -= d[1]//2
        ret += (d[2]+1)//2
    else:
      d[3] = d[3]-d[1]
      ret += d[2]//2
      d[2] = d[2]%2
      if d[2] == 0:
        ret += (d[3]+3)//4
      else:
        if d[3] >= 2:
          ret += 1
          d[3] -= 2
          ret += (d[3]+3)//4
  print('Case #{}: {}'.format(ijk,ret))
