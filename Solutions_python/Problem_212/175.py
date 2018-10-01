#!/usr/bin/env python

T = int(raw_input())
for t in xrange(T):
  N,P = map(int,raw_input().split())
  G = map(int,raw_input().split())
  G = [g for g in G if g % P != 0]
  out = N - len(G)
  while G:
    best = [None for i in xrange(P)]
    for k,g in enumerate(G):
      newbest = best[::]
      for i in xrange(P):
        if best[i] is not None and (newbest[(i + g) % P] is None or len(best[i]) + 1 < len(newbest[(i + g) % P])):
          newbest[(i + g) % P] = best[i] + [k]
        if newbest[g % P] is None:
          newbest[g % P] = [k]
      best = newbest
    out += 1
    if best[0] is None:
      break
    for k in best[0][::-1]:
      del G[k]
  print "Case #%d: %d" % (t+1, out)

