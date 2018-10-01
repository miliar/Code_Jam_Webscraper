'''
Created on 22.05.2010

@author: shelajev
'''

from time import time

filename = 'C-sample'
#filename = 'C-small-attempt1'
#filename = 'C-large'

mod = 100003
z = {}

def combs(n, k):
  if(k > n): return 0
  if(n - k < k): return combs(n, n-k)
  nom = 1;
  denom = 1;
  for i in range(1, k+1):
    nom *= (n+1 - i)
    denom *= i
  return nom // denom

def fillDP():
  for n in range(2, 501):
    print('doing ' + str(n))
    z[(n, 1)] = 1;
    z[(n, n)] = 1;
    for pos in range(2, n+1):
      m = 0
      for spos in range(1, pos):
        nn = n - pos - 1
        k = pos - spos - 1
        r = (z[(pos, spos)]*combs(nn, k) % mod)
        m = (m + r) % mod
      z[(n, pos)] = m



def solve(n):
  v = 0
  for pos in range(1, n+1):
    v = (v + z[(n, pos)]) % mod
  return v

if __name__ == '__main__':
  mytime = -time()
  print(mytime)
  fillDP()
#  for n in range(5, 8):
#    for pos in range(1, n):
#      print(z[(n, pos)]);
  with open(filename + '.in') as file:
    out = open(filename + '.out', 'w')
    C = int(file.readline());
    for i in range(1, C + 1):
      n = int(file.readline())
      r = solve(n)
      tada = 'Case #{0}: {1}\n'.format(i, r)
      out.write(tada)
      print(tada)
  mytime = mytime + time()
  print(mytime/1000)
   