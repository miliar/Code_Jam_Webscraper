#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def solve(s_levels):
  applauding = 0
  friends = 0
  for level, count in enumerate(s_levels):
    if level > applauding:
      new_friends = level - applauding
      friends += new_friends
      applauding += new_friends
    applauding += count
  return friends


if __name__ == "__main__":
  input_filepath = sys.argv[1]

  with open(input_filepath, "rt") as input_file:
    T = int(next(input_file))

    for i in range(1, T + 1):
      line = next(input_file).strip()
      s_max, s_levels = line.split(" ", 1)
      s_max = int(s_max)
      s_levels = tuple(map(int, s_levels))
      assert((s_max + 1) == len(s_levels))
      print("Case #%u: %u" % (i, solve(s_levels)))

    assert(i == T)
