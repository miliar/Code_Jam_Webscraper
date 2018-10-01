C = int(raw_input())
for c in xrange(C):
  N, K, B, T = map(int, raw_input().split())
  X = map(float, raw_input().split())
  V = map(float, raw_input().split())
  
  H = zip(X,V)
  H = [(x,v,(x+v*T >= B)) for x,v in H]
  
  k = 0
  l = 0
  s = 0
  while H:
    x,v,b = H.pop()
    if b:
      k += 1
      s += l
      if k == K:
        break

    else:
      l += 1


  if k==K:
    print 'Case #%d: %d' % (c+1, s)
  else:
    print 'Case #%d: IMPOSSIBLE' % (c+1)
  