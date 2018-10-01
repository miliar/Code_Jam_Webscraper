#!/usr/bin/env python3

def line(C, s):
  if s == '?' * C:
    return None
  else:
    def gen():
      last = '?'
      for c in s:
        last = last if c == '?' else c
        if last != '?':
          yield last
    t = ''.join(gen())
    return t[0] * (C - len(t)) + t

def process(R, C, A):
  def gen():
    last = None
    for r in (line(C, s) for s in A):
      last = last if r is None else r
      if last is not None:
        yield last
  t = list(gen())
  return [t[0]] * (R - len(t)) + t

T = int(input())
for case in range(1, T+1):
  R, C = map(int, input().split())
  A = [input() for _ in range(R)]
  res = '\n'.join(process(R, C, A))
  print("Case #{}:\n{}".format(case, res))

