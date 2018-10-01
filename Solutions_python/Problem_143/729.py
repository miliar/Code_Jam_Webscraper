#!/usr/bin/env python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <carlo@miron.it> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. --Carlo Miron
# ----------------------------------------------------------------------------
import sys, pprint

def log(**kwds):
  if getattr(log, "enabled", 0):
    pprint.pprint(kwds, stream=getattr(log, "to", None))

def solve(a, b, k):
  x = 0
  for i in range(a):
    for j in range(b):
      if i&j < k: x += 1
  return x

def test_cases(tokens):
  token = iter(tokens)
  cases = int(next(token))
  for case in range(cases):
    a = int(next(token))
    b = int(next(token))
    k = int(next(token))
    yield case +1, solve(a, b, k)

if __name__ == "__main__":
  log.enabled = sys.flags.debug
  log.to = sys.stderr
  for case, result in test_cases(sys.stdin.read().split()):
    print("Case #%s: %s" % (case, result))
