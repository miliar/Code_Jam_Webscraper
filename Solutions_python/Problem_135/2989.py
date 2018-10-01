#!/usr/bin/python

num_test_cases = int(raw_input())

for case_number in xrange(1, num_test_cases+1):
  cards = [{}, {}]
  for j in xrange(0, 2):
    answer = int(raw_input())
    for k in xrange(1, 5): # row starts from 1
      line = raw_input()
      if k == answer:
        for c in line.split():
          cards[j][c] = True

  num_matches = 0
  matched_card = 0
  for guess in cards[0]:
    if guess in cards[1]:
      num_matches += 1
      matched_card = guess

  if num_matches == 0:
    print "Case #%d: Volunteer cheated!" % case_number
  elif num_matches == 1:
    print "Case #%d: %s" % (case_number, matched_card)
  else:
    print "Case #%d: Bad magician!" % case_number


