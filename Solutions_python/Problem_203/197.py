for t in range(input()):
  n, m = map(int, raw_input().split())
  res = []
  empty = 0
  for _ in range(n):
    row = raw_input().strip()
    if row == '?'*m:
      empty += 1
    else:
      newrow = ''
      let = next(c for c in row if c != '?')
      for c in row:
        let = c if c != '?' else let
        newrow += let
      res += [newrow] * (empty+1)
      empty = 0
  res += [res[-1]] * (n - len(res))
  print 'Case #%d:' % (t+1)
  print '\n'.join(res)


