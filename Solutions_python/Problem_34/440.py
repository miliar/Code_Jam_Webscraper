#!/usr/bin/python

import sys

def howmany(DD, test):
  matcher = []
  i = 0
  while i < len(test):
    if test[i] != '(':
      matcher.append(set(test[i]))
    else:
      i += 1
      matcher.append(set())
      while test[i] != ')':
        matcher[len(matcher) - 1].add(test[i])
        i += 1
    i += 1
  cand = range(0, len(DD))
  for i in xrange(0, len(matcher)):
    new_cand = []
    for j in xrange(0, len(cand)):
      if DD[cand[j]][i] in matcher[i]:
        new_cand.append(cand[j])
    cand = new_cand
    if len(cand) == 0:
      return 0
  return len(cand)

if __name__ == '__main__':
  if len(sys.argv) != 2:
     print ('Usage: %s file' % sys.argv[0])
     sys.exit(1)

  f = open(sys.argv[1])
  L, D, N =  map(lambda x:int(x), f.readline().split())
  DD = []
  for i in xrange(D):
    DD.append(f.readline().strip())
  for i in xrange(N):
    print ('Case #%d:' % (i + 1)),
    print howmany(DD, f.readline().strip())
