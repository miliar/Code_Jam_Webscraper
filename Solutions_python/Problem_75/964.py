#!/usr/bin/env python

import sys

def parse(line):
  a = line.split()
  C = int(a[0])
  repl = a[1:1+C]
  D = int(a[C+1])
  opp = a[C+2:C+2+D]
  N = int(a[C+2+D])
  s = a[C+2+D+1]
  return (repl, opp, s)

def solve(o):
  replS, oppS, s = o
  if (len(s) < 2):
    return '[%s]' % ', '.join(s)
  repl = dict(map(lambda s: (s[0]+s[1], s[2]), replS))
  repl.update(map(lambda s: (s[1]+s[0], s[2]), replS))
  opp = dict()
  for c1, c2 in map(lambda s: (s[0], s[1]), oppS):
    opp.setdefault(c1, []).append(c2)
    opp.setdefault(c2, []).append(c1)

  res = s[:1]
  oppS = set()
  for c in s[1:]:
    # print "%s %c %s" % (res, c, oppS)
    res+=c
    if (res[-2:] in repl):
      res = res[:-2] + repl[res[-2:]]
    else:
      if (1 < len(res)):
        oppS.update(opp.get(res[-2], []))
      if (res[-1] in oppS):
        res = ''
        oppS = set()

  # print "%s %s" % (res, oppS)

  return '[%s]' % ', '.join(res)

def main():
  N = int(sys.stdin.readline())
  for i in range(N):
    s = sys.stdin.readline().strip()
    # print "Case #%d: %s %s" % (i+1, s, solve(parse(s)))
    print "Case #%d: %s" % (i+1, solve(parse(s)))

if __name__ == '__main__':
  main()
