#!/usr/bin/env python2.7

entry = raw_input()
googlerese = raw_input()
translation = {}
s = set()

for i, char in enumerate(entry):
    if char != ' ':
        s.add((char, googlerese[i]))

for i in s:
    translation[i[1]] = i[0]

print translation
