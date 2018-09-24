#!/usr/bin/python

import sys
f = sys.stdin

cnt = int(f.readline())
for i in range(1, cnt+1):
  engines = []
  queries = []
  #engines_cnt = {}

  for n in range(1, int(f.readline())+1):
    e = f.readline()
    engines.append(e)
    #engines_cnt[e] = 0

  for n in range(1, int(f.readline())+1):
    q = f.readline()
    #if q in queries: continue
    queries.append(q)
    #if engines_cnt.has_key(q): engines_cnt[q]+= 1

  cnt = -1

  cur = 0
  while True:
    maxlen = -1
    for e in engines:
      n = 0
      for q in queries[cur:]:
        if q == e: break
        n+= 1
      if n > maxlen:
        maxlen = n
    cnt+= 1
    cur+= maxlen
    if cur >= len(queries): break

  #engines.sort()
  #queries.sort()

  #engine, cnt = engines_cnt.items()[0]
  #for en, cn in engines_cnt.items():
#    if cnt > cn:
#      cnt = cn
#      engine = en

  print "Case #%i: %i" %(i, cnt)
