from math import *
from itertools import *

filename = 'D-small-attempt1'

# Rooks are x
# Bishops are +
# Queens are o

def maximum_bishops(bishops, n) :
  #Assuming all bishops in top row
  return set((0, c) for c in range(n)) | set((n-1, c) for c in range(1,n-1))

def n_rooks(rooks, n) :
  total = set(range(n))
  rows = total - set(map(lambda x: x[0], rooks))
  cols = total - set(map(lambda x: x[1], rooks))
  return rooks | set(zip(rows, cols))

with open(filename + '.out.txt', 'w') as output_file :
  with open(filename + '.in.txt', 'r') as input_file :
    num_cases = int(input_file.readline())
    for case_number in range(1,num_cases+1) :
      # read inputs
      params = input_file.readline().split()

      n = int(params[0])
      m = int(params[1])

      bishops = set()
      rooks = set()
      queens = set()

      for _ in range(m) :
        tokens = input_file.readline().split()
        piece = tokens[0]
        coords = (int(tokens[1])-1, int(tokens[2])-1)

        if piece == '+' :
          bishops.add(coords)
        elif piece == 'x' :
          rooks.add(coords)
        elif piece == 'o' :
          queens.add(coords)

      # solve
      max_bishops = maximum_bishops(bishops | queens, n)
      max_rooks = n_rooks(rooks | queens, n)
      max_queens = max_bishops & max_rooks

      max_bishops -= max_queens
      max_rooks -= max_queens

      # compute output values
      points = len(max_bishops) + len(max_rooks) + 2 * len(max_queens)
      new_bishops = max_bishops - bishops
      new_rooks = max_rooks - rooks
      new_queens = max_queens - queens
      num_new = len(new_bishops) + len(new_rooks) + len(new_queens)

      # write output
      output_file.write('Case #' + str(case_number) + ': ' + str(points) + ' ' + str(num_new) + '\n')
      for bishop in new_bishops :
        output_file.write('+ ' + str(bishop[0]+1) + ' ' + str(bishop[1]+1) + '\n')
      for rook in new_rooks :
        output_file.write('x ' + str(rook[0]+1) + ' ' + str(rook[1]+1) + '\n')
      for queen in new_queens :
        output_file.write('o ' + str(queen[0]+1) + ' ' + str(queen[1]+1) + '\n')
