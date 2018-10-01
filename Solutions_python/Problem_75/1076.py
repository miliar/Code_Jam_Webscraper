#!/usr/bin/python

from collections import deque, defaultdict
import sys

f = open(sys.argv[1])

case = 0
for line in f:
  if case == 0:
    case += 1
    continue

  tokens = deque(line.split())
  combine = defaultdict(dict)
  oppose = dict()

  C = int(tokens.popleft())
  for i in range(0,C):
    combo = tokens.popleft()
    l = combo[0]
    r = combo[1]
    n = combo[2]
    combine[l][r] = n
    combine[r][l] = n

  D = int(tokens.popleft())
  for i in range(0,D):
    pair = tokens.popleft()
    l = pair[0]
    r = pair[1]
    oppose[l] = r
    oppose[r] = l

  N = tokens.popleft()
  invoc  = tokens.popleft()

  #print invoc

  oppose_set = dict()
  elements = []
  for c in invoc:
    if len(elements) == 0:
      elements.append(c)
      if c in oppose:
        oppose_set[oppose[c]] = 1
    elif c in combine[elements[-1]]:
      tail = elements.pop()
      if tail in oppose and oppose[tail] in oppose_set:
        oppose_set[oppose[tail]] -= 1
        if oppose_set[oppose[tail]] == 0:
          del(oppose_set[oppose[tail]])
      elements.append(combine[tail][c])
    elif c in oppose_set:
      elements = []
      oppose_set = dict()
    else:
      elements.append(c)
      if c in oppose:
        if oppose[c] in oppose_set:
          oppose_set[oppose[c]] += 1
        else:
          oppose_set[oppose[c]] = 1


  print "Case #%d: [%s]" % (case, ', '.join(map(str, elements)))
  case += 1

