import math
from sets import Set
memory = {}

def get_lr(i):
  if not i in memory:
    div,mod = divmod(i,2)
    l = div - 1
    if mod != 0:
      l = div
    r = div
    memory[i] = (l,r)
  return memory[i]

def step(s):
  n = max(s)
  s.remove(n)
  l,r = get_lr(n)
  s.add(r)
  s.add(l)


for cas in xrange(1,1+input()):
  print "Case #%s:" % cas,
  n,k = map(int,raw_input().split())

  if n == k:
    print "0 0"
    continue

  l,r = get_lr(n)

  if k == 1:
    print "%d %d" % (r, l)
    continue
  
  # s = Set([n])

  index = 0

  levels = int(math.floor(math.log(k)/math.log(2)))

  in_level = pow(2,levels)
  dic = {n: 1}

  for lev in range(levels):
    new_dic = {}
    for i in dic:
      l,r = get_lr(i)
      if not l in new_dic:
        new_dic[l] = 0

      if not r in new_dic:
        new_dic[r] = 0

      new_dic[l] += dic[i]
      new_dic[r] += dic[i]

    dic = new_dic
  
  tk = k
  for lev in range(levels):
    tk -= pow(2,lev)

  use_v = max(dic)
  if tk > dic[max(dic)]:
    use_v = min(dic)

  ls,rs = get_lr(use_v)

  print "%d %d" % (max(ls, rs),min(ls, rs))