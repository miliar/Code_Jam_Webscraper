from itertools import *

filename = 'A-small-attempt1'

def is_empty(cell) :
  return cell == '?'

with open(filename + '.out.txt', 'w') as output_file :
  with open(filename + '.in.txt', 'r') as input_file :
    n = int(input_file.readline())
    for case_number in range(1,n+1) :
      params = input_file.readline().split()
      R, C = int(params[0]), int(params[1])
      cake = [list(input_file.readline()) for row in range(R)]

      initialed_cells = set()
      for row in range(R) :
        indexed_row = zip(cake[row], [(row, col) for col in range(C)])
        initialed_cells |= set(filter(lambda x: x[0] != '?', indexed_row))

      for (initial, (row, col)) in initialed_cells :
        up, down, left, right = row-1, row+1, col-1, col+1
        while left >= 0 and is_empty(cake[row][left]) : left -= 1
        while right < C and is_empty(cake[row][right]) : right += 1
        while up >= 0 and all(map(is_empty, cake[up][left+1:right])) : up -= 1
        while down < R and all(map(is_empty, cake[down][left+1:right])) : down += 1
        for r in range(up+1, down) :
          for c in range(left+1, right) :
            cake[r][c] = initial

      output_file.write('Case #' + str(case_number) + ':\n')
      for row in range(R) :
        output_file.write(''.join(cake[row]))