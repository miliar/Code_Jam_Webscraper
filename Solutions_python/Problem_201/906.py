from math import *
from itertools import *

filename = 'C-small-2-attempt0'

def split_cell(size) :
  size = int(size-1)
  half = size // 2;
  rem = size % 2;
  return str(half + rem) + ' ' + str(half)

def find_LR(n, k) :
  wave_index = floor(log(k, 2))
  num_cells = pow(2, wave_index)
  num_dividers = num_cells - 1
  open_stalls = n - num_dividers
  num_large_cells = open_stalls % num_cells
  small_cell_size = open_stalls // num_cells
  if k - num_dividers > num_large_cells :
    return split_cell(small_cell_size)
  else :
    return split_cell(small_cell_size + 1)

def find_answer(line) :
  params = line.split()
  return find_LR(int(params[0]), int(params[1]))

with open(filename + '.out.txt', 'w') as output_file :
  with open(filename + '.in.txt', 'r') as input_file :
    n = int(input_file.readline())
    for case_number in range(1,n+1) :
      answer = find_answer(input_file.readline())
      output_file.write('Case #' + str(case_number) + ': ' + answer + '\n')
