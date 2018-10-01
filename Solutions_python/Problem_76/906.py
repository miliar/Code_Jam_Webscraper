#!/usr/bin/python
import sys

def calc_part(part, l):
  res1 = 0
  res1x = 0
  res2 = 0
  res2x = 0
  for i in xrange(len(l)):
    if part[i]:
      res1x ^= l[i]
      res1 += l[i]
    else:
      res2x ^= l[i]
      res2 += l[i]
  if res1x == res2x:
    return max(res1, res2)
  return None

def calc(l):
  part = [False] * len(l)
  part[0] = True
  stop = False
  max  = None
  while not stop:
    res = calc_part(part, l)
    if res is not None and (max is None or res > max):
      max = res
    for i in xrange(len(part)):
      part[i] = not part[i]
      if part[i]:
        break
    for i in xrange(len(part)):
      if not part[i]:
        break
    else:
      stop = True
  if max is None:
    return "NO"
  return max

def main():
  f = file(sys.argv[1])
  n = int(f.readline())
  for j in xrange(1, n+1):
    t = int(f.readline())
    l = [int(e) for e in f.readline().split()]
    print "Case #%d: %s" % (j, calc(l))

main()
