from collections import deque
def solve(zi):
  n, k = map(int, input().split())
  Q = deque()
  Q.append(n)
  rnd = {n: 1}
  while True:
    l = Q.popleft()
    if l == 0:
      raise 'What?'
    rn = rnd[l]
    ll, rl = l//2, (l-1)//2
    if k <= rn:
      print('Case #%d: %d %d'%(zi+1, ll, rl))
      break
    k -= rn
    for sl in [ll, rl]:
      if sl in rnd:
        rnd[sl] += rn
      else:
        Q.append(sl)
        rnd[sl] = rn

zn = int(input())
for zi in range(zn):
  solve(zi)
