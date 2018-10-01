#!/usr/bin/env python

import string
import sys

known_plaintext = """
a zoo
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""
known_ciphertext = """
y qee
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

known_plaintext = ''.join(known_plaintext.split())
known_ciphertext = ''.join(known_ciphertext.split())

k = {}
for p, c in zip(known_plaintext, known_ciphertext):
    if c in k:
        assert k[c] == p
    k[c] = p

# There's one unknown
assert len(k) == 25

alphabet = frozenset(chr(c) for c in range(ord('a'), ord('z') + 1))
cipher_set = frozenset(k.keys())
plain_set = frozenset(k.values())
missing_cipher = alphabet.difference(cipher_set)
missing_plain = alphabet.difference(plain_set)
assert len(missing_cipher) == len(missing_plain) == 1
k[list(missing_cipher)[0]] = list(missing_plain)[0]

t = string.maketrans(''.join(k.keys()), ''.join(k.values()))

N = int(sys.stdin.readline())
for case in range(N):
    cipher = sys.stdin.readline().strip()
    plaintext = cipher.translate(t)
    print "Case #%i: %s" % (case + 1, plaintext)
