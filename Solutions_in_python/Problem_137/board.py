#!/usr/bin/env python
from sys import argv

def full_mine(r, c):
  if r == 1:
    return one_row(c, 0)
  else:
    return extend(full_mine(r - 1, c), one_row(c, 0))

def one_row(s, n):
  return [[0 if i < n else 1 for i in range(s)]]
def two_row(s, n):
  return extend(one_row(s / 2, n / 2), one_row(s / 2, n / 2))

def embed(inner, outer):
  #print inner
  #print outer
  for i in range(len(inner)):
    for j in range(len(inner[i])):
      #print i, j
      outer[i][j] = inner[i][j]
  return outer

def extend(up, down):
  return up + down

def transpose(m):
  mt = []
  for i in range(len(m)):
    for j in range(len(m[i])):
      while not len(mt) > j:
        mt.append([])
      while not len(mt[j]) > i:
        mt[j].append([])
        
      mt[j][i] = m[i][j]
  return mt
sample = {}
sample[1] = [[0]]
sample[4] = [[0, 0], [0, 0]]
sample[6] = [[0, 0, 0], [0, 0, 0]]
sample[8] = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
sample[9] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sample[10] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1]]
sample[11] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
sample[12] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

sample[13] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]]
sample[14] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1]]
sample[15] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
sample[16] = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
  
def dispatch(r, c, n):
  if n < 0:
    return None
  if n == 0:
    #return full_mine(r, c)
    return None
  if n == 1:
    m = full_mine(r, c)
    m = embed([[0]], m)
    return m
    
  small = min(r, c)
  large = max(r, c)
  is_transpose = small == c
  
  if small == 1:
    m = one_row(r * c, n)
    if is_transpose:
      m = transpose(m)
    return m
  elif small == 2:
    if not n % 2 == 0:
      return None
    if n < 4:
      return None
      
    m = two_row(r * c, n)
    if is_transpose:
      m = transpose(m)
    return m
    
    
  if n in [2, 3, 5, 7]:
    return None
  if small == 3:
    if n > 12:      
      m1 = one_row(small, small)
      m2 = dispatch(small, large - 1, n - small)
      m2 = transpose(m2)
      m = extend(m1, m2)
      if not is_transpose:
        m = transpose(m)
      return m
    else:
      m = full_mine(small, large)
      m = embed(sample[n], m)
      if is_transpose:
        m = transpose(m)
      return m
  elif small == 4:
    if n > 16:      
      m1 = one_row(small, small)
      m2 = dispatch(small, large - 1, n - small)
      m2 = transpose(m2)
      m = extend(m1, m2)
      if not is_transpose:
        m = transpose(m)
      return m
    else:
      m = full_mine(small, large)
      m = embed(sample[n], m)
      if is_transpose:
        m = transpose(m)
      return m
  else:
    if n <= (small - 1) * large:
      m1 = dispatch(small - 1, large, n)
      m2 = one_row(large, 0)
      m = extend(m1, m2)
      if is_transpose:
        m = transpose(m)
      return m
    if n >= 4 * large:
      m1 = two_row(large * 2, large * 2)
      m2 = dispatch(small - 2, large, n - large * 2)
      m = extend(m1, m2)
      if is_transpose:
        m = transpose(m)
      return m

def print_board(m):
  if not m:
    print 'Impossible'
  else:
    b = [['.' if c == 0 else '*' for c in l] for l in m]
    b[0][0] = 'c'
    for l in b:
      print ''.join(l)
    

if __name__ == '__main__':
  fn = argv[1]
  f = open(fn)
  total = int(f.readline().strip())
  for i in range(total):
    print 'Case #%d:' % (i + 1)
    r, c, m = f.readline().split()
    r, c, m = int(r), int(c), int(m)
    b = dispatch(r, c, r * c - m)
    
    print_board(b)
    if not b:
      #print r, c, m
      #print r * c - m
      pass
