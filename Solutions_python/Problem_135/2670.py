#!/usr/bin/env python3
# coding: utf-8

import sys

if __name__ == '__main__':
  data = sys.stdin.read().splitlines()
  cases = [
      [ int(data[i]),
        [
          [int(z) for z in u.split()]
          for u in data[i+1:i+5]
        ]
      ]
    for i in range(1,len(data),5)
    ]
  for i in range(int(data[0])):
    l = [z for z in cases[2*i][1][cases[2*i][0]-1] if z in cases[1+2*i][1][cases[1+2*i][0]-1]]
    x = 'Bad magician!'
    if len(l) == 0: x = 'Volunteer cheated!'
    if len(l) == 1: x = '{}'.format(l[0])
    print('Case #{}: {}'.format(i+1,x))
