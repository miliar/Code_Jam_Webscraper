#!/usr/bin/env python
# coding: utf-8

d = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'q': 'z', 'z': 'q', ' ': ' '}

def decode(s):
  return "".join(map(str, [d[c] for c in s]))

for case in range(int(input())):
  print("Case #{0}: {1}".format(case+1, decode(input())))
