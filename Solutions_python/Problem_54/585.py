'''
Created on 08.05.2010

@author: shelajev
'''

from fractions import gcd

filename = 'B-large'
#filename = 'B-sample'

def lgcd(list):
  acc = list[0]
  for e in list:
    acc = gcd(acc, e)
  return acc

def solve(N, e):
  e.sort()
  d = [];
  prev = e[0]
  for i in range(1, len(e)):
    next = e[i]
    d.append(next-prev)
    prev = next
  d.sort()
  r = lgcd(d)
  r2 = lgcd(e)
  if r == r2: return 0
  return r - (e[0] % r)


if __name__ == '__main__':
  with open(filename + '.in') as file:
    out = open(filename + '.out', 'w')
    C = int(file.readline());
    for i in range(1, C + 1):
      line = file.readline().strip().split(' ')
      N = int(line[0])
      e = list(map(int, line[1:]))
      r = solve(N, e)
      z = 'Case #{0}: {1}\n'.format(i, r)
      out.write(z)
      print(z)
       
       
