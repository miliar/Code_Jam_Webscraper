
class Itv(object):
  def __init__(this, st, ed, tp):
    this.st = st
    this.ed = ed
    this.tp = tp

def solve():
  n, m = input().split()
  n = int(n)
  m = int(m)
  itv = []
  for i in range(n):
    st, ed = input().split()
    itv.append(Itv(int(st), int(ed), 0))
  for i in range(m):
    st, ed = input().split()
    itv.append(Itv(int(st), int(ed), 1))

  if n+m == 0:
    return 1

  itv.sort(key = lambda x: x.st)
  itv.append(Itv(itv[0].st + 1440, itv[0].ed + 1440, itv[0].tp))
  space = [[], []]
  free = 0

  rem = [720, 720]
  ans = 0
  #if itv[0].st > 0:
  #  space[itv[0].tp].append(itv[0].st)
  #print(list((i.st, i.ed, i.tp) for i in itv))
  for i in range(n+m):
    #print( itv[i].tp , itv[i+1].tp)
    if itv[i].tp == itv[i+1].tp:
      space[itv[i].tp].append(itv[i+1].st - itv[i].ed)
    else:
      free += itv[i+1].st - itv[i].ed
      ans += 1

  for i in range(n+m):
    rem[itv[i].tp] -= itv[i].ed - itv[i].st
  
  #print(rem, free, space)
  #print(rem[0] + rem[1])
  #print(free + sum(space[0]) + sum(space[1]))
  #print(ans)

  space[0].sort(reverse = True)
  space[1].sort(reverse = True)

  if sum(space[0]) + free < rem[0]:
    x = rem[0] - sum(space[0]) - free
    for s in space[1]:
      x -= s
      ans += 2
      if x <= 0: break
  elif sum(space[1]) + free < rem[1]:
    x = rem[1] - sum(space[1]) - free
    for s in space[0]:
      x -= s
      ans += 2
      if x <= 0: break
  return ans

zn = int(input())
for zi in range(zn):
  print('Case #%d: %d'%(zi+1, solve()))

