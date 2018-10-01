for T in range(input()):
  d, n = map(int, raw_input().split())
  t = 0
  for _ in range(n):
    k, s = map(int, raw_input().split())
    t = max(t, 1.0 * (d - k) / s)
  print 'Case #%d: %.9f' % (T+1, 1.0 * d / t)
