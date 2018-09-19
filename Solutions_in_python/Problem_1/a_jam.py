#!/usr/bin/python

def searchEngine(engines, searches):
  found = set()
  result = 0
  
  for search in searches:
    # go through searches greedily
    if search not in found:
      found.add(search)
      
    if len(found) == len(engines):
      found = set([search])
      result += 1
  return result

N = int(raw_input())

for i in range(1, N+1):
  # get S
  S = int(raw_input())
  
  # get search engines
  engs = []
  for ii in range(S):
    engs.append(raw_input())
  
  # get Q
  Q = int(raw_input())
  
  # get searches
  querys = []
  for ii in range(Q):
    querys.append(raw_input())
  
  
  print 'Case #%d: %d' % (i, searchEngine(engs, querys)) 






