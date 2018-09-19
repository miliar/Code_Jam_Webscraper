#!/usr/bin/python2.5

import re
import sys

L, D, N = (int(x) for x in sys.stdin.readline().split())
vocab = tuple(sys.stdin.readline().strip() for i in xrange(D))
tests = tuple(sys.stdin.readline().strip() for i in xrange(N))
regexps = tuple(re.compile(x.replace("(", "[").replace(")", "]")) for x in tests)

for i, r in enumerate(regexps):
  result = sum(1 for v in vocab if r.match(v))
  print "Case #%d: %d" % (i + 1, result)
