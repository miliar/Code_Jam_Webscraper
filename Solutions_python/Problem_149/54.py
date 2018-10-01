from collections import defaultdict

def simlist(lst):
  t = sorted(lst)
  ret = []
  for elm in lst:
    for i in xrange(len(lst)):
      if t[i] == elm: ret.append(i)
  return ret

def getans(v1, v2, n):
  m = {}
  for i in xrange(n):
    m[v2[i]] = i
  for i in xrange(n):
    v1[i] = m[v1[i]]

  cnt = 0
  for i in xrange(n):
    for j in xrange(i + 1, n):
      if v1[i] > v1[j]: cnt += 1
  return cnt


def solve(tcase):
  n = int(raw_input())
  lst = [int(t) for t in raw_input().split()]
  lst = simlist(lst)
  maxn, maxp = -1, -1
  
  lst2 = sorted(lst)
  ans, lt, rt = 0, 0, n - 1
  
  ret = [0] * n
  for elm in lst2:
    p = -1
    for i in xrange(n):
      if lst[i] == elm: p = i
    ld = abs(p - lt)
    rd = abs(p - rt)
    if ld <= rd: ret[lt] = elm; lt += 1
    else: ret[rt] = elm; rt -= 1
  print ret
  ans = getans(lst, ret, n)

  print 'Case #%d: %d' % (tcase, ans)

T = int(raw_input())
for tcase in xrange(1, T + 1):
  solve(tcase)
