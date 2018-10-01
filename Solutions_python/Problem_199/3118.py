#!/usr/bin/env python3

import sys

POS='+'
NEG='-'

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    s, k = read_input(fi)
    solution = solve(s, k)
    display_and_clear(fo, i, solution)

def read_input(f):
  s, arg = f.readline().split()
  k = int(arg)
  return s, k

def display_and_clear(f, i, count):
  solution = count if count >= 0 else 'IMPOSSIBLE'
  f.write('Case #%d: %s\n' % (i, solution))
  f.flush()

def solve(s, k):
  count = 0
  s = list(s)
  length = len(s)

  for i in range(length - k + 1):
    if s[i] == NEG:
      flip(s, k, i)
      count += 1

  for i in range(length - k + 1, length):
    if s[i] != POS:
      return -1

  return count

def flip(s, k, begin):
  for i in range(k):
    ch_ind = begin + i
    if s[ch_ind] == NEG:
      s[ch_ind] = POS
    else:
      s[ch_ind] = NEG

if __name__ == '__main__':
  main()

