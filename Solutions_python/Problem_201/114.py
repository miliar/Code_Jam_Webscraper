import sys
import itertools
import heapq
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, k ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  y, z = None, None
  cfg = [ -N ]
  cnt = { N: 1 }
  heapq.heapify(cfg)
  while k:
    v = -heapq.heappop(cfg)
    cnt_v = cnt[v]
    del cnt[v]
    y, z = v/2, v-1-v/2
    nb = min(k, cnt_v)
    for u in [ y, z ]:
      if u in cnt: cnt[u] += nb
      else:
        heapq.heappush(cfg, -u)
        cnt[u] = nb
    k -= nb

  print "Case #%d: %d %d" % (1+tmp_tc, y, z)

