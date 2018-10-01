#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')
f.readline()

case = 0

for l in f.readlines():
  l = l.strip()
  k = l.split(' ')

  case  += 1
  trans  = {}
  opp    = {}

  #transformations
  c = int(k.pop(0))
  while(c > 0):
    c -= 1
    t = k.pop(0)
    if not t[0] in trans:
      trans[t[0]] = {}
    if not t[1] in trans:
      trans[t[1]] = {}
    trans[t[0]][t[1]] = t[2]
    trans[t[1]][t[0]] = t[2]

  #removals
  r = int(k.pop(0))
  while(r > 0):
    r -= 1
    t = k.pop(0)
    if not t[0] in opp:
      opp[t[0]] = []
    if not t[1] in opp:
      opp[t[1]] = []
    opp[t[0]].append(t[1])
    opp[t[1]].append(t[0])

  n = int(k.pop(0))
  elements = list(k.pop(0))
  final = []
  final.append(elements.pop(0))
  while elements:
    e = elements.pop(0)
    if final:
      if e in trans and final[-1] in trans[e]:
        final.append(trans[e][final.pop()])
      elif e in opp:
        for w in final:
          if w in opp[e]:
            final = []
            break
        if final:
          final.append(e)
      else:
        final.append(e)
    else:
      final.append(e)

  finalstr = str(final).replace('\'', '')
  print("Case #{0}: {1}".format(case, finalstr))
