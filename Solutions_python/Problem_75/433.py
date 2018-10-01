#!/usr/bin/env python2.7

from collections import defaultdict

cases = int(raw_input())

for i in range(cases):
  bits = raw_input().split()
  C = int(bits.pop(0))
  combinations = {}

  for j in range(C):
    base1, base2, result = bits.pop(0)
    combinations[tuple(sorted([base1, base2]))] = result

  D = int(bits.pop(0))
  opposed = defaultdict(set)

  for j in range(D):
    base1, base2 = bits.pop(0)
    opposed[base1].add(base2)
    opposed[base2].add(base1)

  N = int(bits.pop(0))
  st = bits.pop(0)
  invoked = []

  for j in range(N):
    next_ch = st[j]

    if invoked:
      comb_key = tuple(sorted([next_ch, invoked[-1]]))

      if comb_key in combinations:
        invoked.pop()
        invoked.append(combinations[comb_key])
      else:
        invoked.append(next_ch)

        for ch in invoked:
          if ch in opposed[next_ch]:
            invoked = []
            break

    else:
      # first char
      invoked.append(next_ch)

  print "Case #%d: [%s]" % (i + 1, ", ".join(ch for ch in invoked))
