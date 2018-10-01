def solve(tcase):
  smax, s = raw_input('').split()
  ret, cnt = 0, int(s[0])
  for i in xrange(1, len(s)):
    new = int(s[i])
    need = i
    if cnt < need:
      ret += (need - cnt)
      cnt = need
    cnt += new

  print 'Case #%d: %s' % (tcase, ret)

T = int(raw_input(''))
for tcase in xrange(1, T + 1):
  solve(tcase)