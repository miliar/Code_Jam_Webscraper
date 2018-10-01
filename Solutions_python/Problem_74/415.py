#!/usr/bin/env python2.7

cases = int(raw_input())

for i in range(cases):
  bits = raw_input().split()
  buttons = int(bits.pop(0))
  pos = {"O": 1, "B": 1}
  other = {"O": "B", "B": "O"}
  reserve = {"O": 0, "B": 0}
  steps = 0

  for j in range(buttons):
    col = bits.pop(0)
    num = int(bits.pop(0))
    need = abs(pos[col] - num)

    # move to button
    while need > 0:
      if reserve[col] > 0:
        reserve[col] -= 1
        need -= 1
      else:
        reserve[other[col]] += 1
        steps += 1
        need -= 1

    # push button
    reserve[other[col]] += 1
    reserve[col] = 0
    steps += 1

    pos[col] = num

  print "Case #%d: %d" % (i + 1, steps)
