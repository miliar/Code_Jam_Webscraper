#! /usr/bin/python

import sys
import copy


def do_new_count(sentence):
  # stores (index in target phrase, index in sentence) -> count of sentences that can be made
  # with this letter/position as the start of the suffix
  storage = [{} for x in xrange(0, len(chars))]
  for i in xrange(len(sentence) - 1, -1, -1): # len -> 0
    c = sentence[i]
    for j, char in enumerate(chars):
      if c == char:
        # figure out what the count is for any next letters that come later in the sentence
        count = 0
        #print "[%d][%d]" % (j, i)
        if (j + 1 < len(chars)):
          positions = storage[j + 1]
          for k in positions:
            # step through the possible next letters
            if k > i:
              #print k
              count += positions[k]
        else:
          #print "end"
          count = 1
        #print "= %d" % (count)
        storage[j][i] = count

  final_count = 0
  for k in storage[0]:
    final_count += storage[0][k]
  #print "%r" % zip(chars, storage)
  return final_count

filename = sys.argv[1]
lines = open(filename).readlines()
lines.pop(0)
case_num = 1
chars = []
for c in "welcome to code jam":
  chars.append(c)
for line in lines:
  sentence = line.strip()
  count = do_new_count(sentence)
  print "Case #%d: %04d" % (case_num, count % 10000)
  case_num += 1
