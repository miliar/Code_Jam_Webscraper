from __future__ import print_function
import numpy as np # learn more: https://python.org/pypi/numpy
from copy import deepcopy

mp = {'+':1, 'x':2, 'o':3, ' ': 0}
mp_rev = { v:k for k,v in mp.items() }
def split_matrix(m):
  a = deepcopy(m)
  b = deepcopy(m)
  for f, r, mat in ((1, 2, a), (2, 1, b)):
    for i, row in enumerate(mat):
      mat[i] = [{f:f, r:0, 3:f, 0:0}[e] for e in row]
  return a, b

def get_diag_indices(N, i, j):
  _i, _j = i, j
  while _i > 0 and _j > 0:
    _i -= 1
    _j -= 1
    yield _i, _j
  _i, _j = i, j 
  while _i < N-1 and _j < N-1:
    _i += 1
    _j += 1 
    yield _i, _j
  _i, _j = i, j 
  while _i < N-1 and _j > 0:
    _i += 1
    _j -= 1 
    yield _i, _j
  _i, _j = i, j 
  while _i > 0 and _j < N-1:
    _i -= 1
    _j += 1 
    yield _i, _j
    
def populate_mask_plus(m, N):
  mask = np.zeros((N, N))
  for row in range(N):
    for col in range(N):
      if m[row, col] == mp['+']:
        mask[row, col] = 2
        for ind in get_diag_indices(N, row, col):
          mask[ind] = 1
  return mask

def populate_mask_x(m, N):
  mask = np.zeros((N, N))
  for row in range(N):
    for col in range(N):
      if m[row, col] == mp['x']:
        mask[row, :] = 1
        mask[:, col] = 1
        mask[row, col] = 2
  return mask
    
def add_plus(m, N):
  m[0, :] = mp['+']
  mask = populate_mask_plus(m, N)
  while True:
    placed = False
    for row in (0, N-1):#range(N):
      for col in range(N):
        if mask[row, col] == 0:
          m[row, col] = mp['+']
          mask[row, col] = 2
          placed = True
          for ind in get_diag_indices(N, row, col):
            mask[ind] = 1
    if not placed:
      break
  return mask
  
def add_x(m, N):
  mask = populate_mask_x(m, N)
  while True:
    placed = False
    for row in range(N):
      for col in range(N):
        if mask[row, col] == 0:
          m[row, col] = mp['x']
          mask[row, col] = 2
          placed = True
          mask[row, :] = 1
          mask[:, col] = 1
    if not placed:
      break
  return mask
  
def combine_matrix(plus, x):
  return plus+x
  
def find_moves(combined, orig, N):
  diff = combined - orig
  #print(diff)
  for row in range(N):
    for col in range(N):
      if diff[row, col] != 0:
        yield "{} {} {}".format(mp_rev[combined[row, col]], row+1, col+1)

T = int(raw_input())
for c in range(T):
  N, M = map(int, raw_input().split(" "))
  matrix = np.zeros((N,N))
  for _ in range(M):
    val, row, col = raw_input().split(" ")
    row, col = int(row)-1, int(col)-1
    matrix[row, col] = mp[val]
  plus_matrix, x_matrix = split_matrix(matrix)
  plus_matrix = np.array(plus_matrix)
  x_matrix = np.array(x_matrix)
  add_plus(plus_matrix, N)
  add_x(x_matrix, N)
  #print(matrix)
  #print(plus_matrix)
  #print(x_matrix)
  cmb = combine_matrix(plus_matrix, x_matrix)
  #print(cmb)
  moves = list(find_moves(cmb, matrix, N))
  print("Case #{}: {} {}".format(c+1, int(plus_matrix.sum()+x_matrix.sum()/2), len(moves)))
  if moves:
    print(*moves, sep='\n')