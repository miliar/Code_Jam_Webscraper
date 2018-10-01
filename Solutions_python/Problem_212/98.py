for t in range(input()):
  n, p = map(int, raw_input().split())
  g = [x % p for x in  map(int, raw_input().split())]
  cnt = [g.count(i) for i in range(p)]
  res = cnt[0]
  if p == 2:
    res += (cnt[1] + 1) / 2
  elif p == 3:
    res += min(cnt[1], cnt[2]) + (max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]) + 2) / 3
  else:
    x = min(cnt[1], cnt[3])
    res += x
    cnt[1] -= x
    cnt[3] -= x
    x = cnt[2] / 2
    res += x
    cnt[2] -= 2*x
    if cnt[1] == 0:
      cnt[1] = cnt[3]
    if cnt[2] == 1:
      if cnt[1] > 2:
        res += 1
        cnt[1] -= 2
        cnt[2] -= 1
    res += (cnt[1] + 3) / 4
    if cnt[1] % 4 == 0 and cnt[2]:
      res += 1
  print 'Case #%d: %d' % (t+1, res)
