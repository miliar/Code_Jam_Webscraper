#!/usr/bin/env python

N = int(raw_input())
phrase = "welcome to code jam"
for case in xrange(1, N+1):
  text = raw_input()
  dp = [[0] * (len(phrase)+1) for i in xrange(len(text)+1)]
  for i in xrange(len(text)):
    dp[0][0] = dp[i+1][0] = 1
    for j in xrange(len(phrase)):
      if text[i] == phrase[j]:
        dp[0][j+1] += dp[0][j]
        dp[0][j+1] %= 10000
  ans = sum([row[-1] for row in dp])
  print "Case #%d: %04d" % (case, ans)
