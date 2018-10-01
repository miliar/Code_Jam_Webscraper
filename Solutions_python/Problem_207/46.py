for T in range(input()):
  x = map(int, raw_input().split())[1::2]
  a, b, c = sorted(range(3), key=x.__getitem__)
  print 'Case #%d:' % (T+1),
  if x[c] > x[a]+x[b]:
    print 'IMPOSSIBLE'
  else:
    t = [-1]
    while x[a]+x[b]+x[c] > 0:
      if x[c] and t[-1] != c:
        t.append(c)
      else:
        t.append(max((a, b), key=x.__getitem__))
      x[t[-1]] -= 1
    print ''.join('RYB'[i] for i in t[1:])
