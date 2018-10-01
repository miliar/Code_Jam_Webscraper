#!/usr/bin/env python

from sys import stdin

TC = int(stdin.readline().strip())
for tc in xrange(1, TC+1):
   R, k, N = map(int, stdin.readline().split())
   g = map(int, stdin.readline().split())
   res = 0
   vis = [-1] * N
   sums = [0] * N
   supt = [0] * N
   path = []
   cur = 0
   for r in xrange(R):
      if vis[cur] >= 0:
         m = (R - r) / (r-vis[cur])
      #  print '* r = %d  m = %d  cur = %d  res = %d  vis[cur] = %d' % (r, m, cur, res, vis[cur])
         res += m * (res - supt[cur])
         rem = (R - r) % (r-vis[cur])
         if rem > 0:
            for i in xrange(vis[cur], vis[cur]+rem):
               res += sums[ path[i] ]
         break
      vis[cur] = r
      supt[cur] = res
      path.append(cur)
      nxt = cur
      sum = 0
      for i in xrange(N):
         if sum + g[nxt] > k:
            break
         sum += g[nxt]
         nxt += 1
         if nxt >= N:
            nxt = 0
      res += sum
      sums[cur] = sum
      cur = nxt
   print 'Case #%d: %d' % (tc, res)