from bisect import bisect_left
for c in xrange(int(raw_input())):
  n = int(raw_input())
  vines = []
  dists = []
  for i in xrange(n):
    inp = map(int, raw_input().split())
    vines.append(inp[0])
    dists.append(inp[1])
  d = int(raw_input())
  vines.append(d)
  dists.append(0)
  maxi = [-1]*(n+1)
  maxi[0] = vines[0]
  for i in xrange(n):
 #   print i, maxi
    if maxi[i] == -1:
      break
    last = bisect_left(vines, vines[i]+maxi[i]+1)
    for j in xrange(i + 1, last):
      maxi[j] = max(maxi[j], min(vines[j]-vines[i], dists[j]))
  else:
    if maxi[-1]>=0:
      print "Case #%d: YES" %(c+1)
    else:
      print "Case #%d: NO" %(c+1)
    continue
  print "Case #%d: NO" %(c+1)
