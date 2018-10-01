#!/usr/bin/env python2

def element_is_valid(matrix, (row, col)):
  element = matrix[row][col]
  horizontal = min(matrix[row])
  vertical = min([matrix[i][col] for i,row in enumerate(matrix)])
  return element == horizontal or element == vertical

def matrix_transform(matrix):
  m = max([max(row) for row in matrix])
  return [[(m - e) for e in row] for row in matrix]

def matrix_is_valid(matrix):
  matrix = matrix_transform(matrix)
  elements = []
  for i,row in enumerate(matrix):
    for j,col in enumerate(matrix[i]):
      elements.append(element_is_valid(matrix, (i, j)))
  return reduce(lambda x, y: x and y, elements)


def read_entry(input_file):
  entry = []
  rows_n, cols_n = [int(f) for f in input_file.readline().strip().split()]
  for i in xrange(rows_n):
    cols = [int(e) for e in input_file.readline().split()]
    entry.append(cols)
    assert(len(cols) == cols_n)
  return entry

def process_entry(entry):
  codes = {
      True:   'YES',
      False:  'NO',
      }
  is_valid = matrix_is_valid(entry)
  return codes[is_valid]

def decode_input(input_file):
  results = []

  entries = int(input_file.readline().strip())

  for i in xrange(entries):
    entry = read_entry(input_file)
    results.append(process_entry(entry))

  i = 1
  for r in results:
    print('Case #%d: %s' % (i, r))
    i += 1



if __name__ == '__main__':
  import sys
  
  if len(sys.argv) > 1:
    decode_input(open(sys.argv[1]))
