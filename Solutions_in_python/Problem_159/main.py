#!/usr/bin/python

import fileinput

def solve(num):
  if len(num) < 2:
    return 0, 0
  x = 0
  last = -1
  max_diff = 0
  for n in num:
    if last is -1:
      pass
    else:
      if n < last:
	x += last - n
        if last - n > max_diff:
	  max_diff = last - n
    last = n
  speed = 1.0 * max_diff / 10
  last = -1
  y = 0
  for n in num[:len(num) - 1]:
    if n < max_diff:
      y += n
    else:
      y += max_diff

  return x,y


    

if __name__ == '__main__':
  fin = fileinput.input()
  t = int(fin.readline())
  for i in range(t):
    out = None
    n = int(fin.readline())
    num = [int(_i) for _i in fin.readline().strip().split()]
    x, y = solve(num)
    print 'Case #{0}: {1} {2}'.format(i + 1, x, y)
