#!/usr/bin/env python

import sys

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

sys.stdin = open("a_in")
sys.stdout = open("a_out", "w")

case_count = int(raw_input())
for case in xrange(case_count):
    word, n = raw_input().split()
    n = int(n)

    size = len(word)
    w = -1

    sub_count = 0
    for i in xrange(size):
        # print i, w
        if i > w:
            # find a new slot for window
            slot_found = False
            for w in xrange(i, size - n + 1):
                slot_found = True
                # print word[w:w + n]
                for letter in word[w:w + n]:
                    if letter in vowels:
                        slot_found = False
                if slot_found:
                    break
            # print "Slot: " + str(w) + " " + word[w:w + n]
            # print slot_found
            if not slot_found:
                break
            else:
                # print "Added: %s" % (size - (w + n) + 1)
                combos = size - (w + n) + 1
                sub_count += combos
        else:
            # print "Added: %s" % (size - (w + n) + 1)
            combos = size - (w + n) + 1
            sub_count += combos

    print "Case #%s: %s" % (case + 1, sub_count)
