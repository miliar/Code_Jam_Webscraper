for cas in xrange(1, input()+1):
  print "Case #%d:" % cas,
  N, P = map(int, raw_input().split())
  ans1 = 0
  x = 2 ** (N-1)
  i = 2
  pos = 1
  ind = 0
  while x > 0:
    pos += x
    ind += i
    if pos <= P:
      ans1 = ind
    x >>= 1
    i <<= 1
  print min(ans1, 2**N - 1),
  ans2 = 0
  x = 2 ** (N-1)
  ind = 0
  pos = 1
  while x > 0:
    ind += x
    pos *= 2
    if pos <= P:
      ans2 = ind
    x >>= 1
  print ans2
