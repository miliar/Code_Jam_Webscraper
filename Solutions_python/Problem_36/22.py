#!/usr/bin/python

import collections

rl = raw_input

n = int(rl())
phrase = list(enumerate("welcome to code jam"))
for x in xrange(1,n+1):
  s = rl()
  cnt = collections.defaultdict(int)
  cnt[-1] = 1
  for ch in s:
    for i,pch in phrase:
      if ch == pch:
        cnt[i] += cnt[i-1]
        cnt[i] %= 10000
  print "Case #%d: %04d" % (x,cnt[18])

