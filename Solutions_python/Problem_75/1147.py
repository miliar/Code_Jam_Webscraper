#!/usr/bin/env python

tests = input()

from collections import defaultdict

for test in range(tests):
  line = raw_input().strip().split(' ')
  i = 0
  C = int(line[i])
  combine = line[i+1:i+C+1]
  i = i+C+1
  D = int(line[i])
  destroy = line[i+1:i+D+1]
  i = i+D+1
  N = int(line[i])
  cards = line[-1]
  assert(len(cards) == N)

  inlist = defaultdict(int)
  rejects = {}
  constructs = {}
  # preprocess dict of pairs of elements that reject
  for pair in destroy:
    rejects[pair[0]] = pair[1]
    rejects[pair[1]] = pair[0]
  for trip in combine:
    constructs[trip[1::-1]] = constructs[trip[0:2]] = trip[2]

  deck = []
  for card in cards:
    deck.append(card)
    inlist[card] += 1
    # combine?
    while len(deck) >= 2:
      lasttwo = ''.join(deck[-2:])
      if lasttwo in constructs:
        for card2 in lasttwo:
          inlist[card2] -= 1
        deck[-2:] = [constructs[lasttwo]]
      else:
        break

    if deck[-1] in rejects and inlist[ rejects[deck[-1]] ] > 0:
      del deck[:]
      inlist.clear()
      continue

  print 'Case #{0}: [{1}]'.format(test+1, ', '.join(deck))
