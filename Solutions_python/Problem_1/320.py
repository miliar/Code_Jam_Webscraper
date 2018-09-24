#! /usr/bin/python

fd = open("input.in")

total = int(fd.readline())

for i in range(0,total):
  num_engine = int(fd.readline())
  engine = {}
  for j in range(0,num_engine):
    engine[fd.readline()] = 1

  num_search = int(fd.readline())
  search = []
  for j in range(0,num_search):
    search += [fd.readline()]

  kept_engine = engine.copy()

#  print engine
#  print search

  best_min = 2 ** 24

  for b,q in engine.iteritems():
    for k, v in kept_engine.iteritems():
      kept_engine[k] = 1
    kept_engine[b] = 0
    num_kept_engine = num_engine - 1
    switch = 0

    for pos in range(0,num_search):
#      print pos, switch, num_kept_engine, kept_engine
      if kept_engine[search[pos]] == 1:
        kept_engine[search[pos]] = 0
        num_kept_engine -= 1
      if num_kept_engine == 0:
        switch += 1
        for k, v in kept_engine.iteritems():
          kept_engine[k] = 1
        kept_engine[search[pos]] = 0
        num_kept_engine = num_engine - 1
    if switch < best_min:
      best_min = switch 

  print "Case #%d: %d" % (i + 1, best_min)
 
