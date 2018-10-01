#!/usr/bin/python -t

import sys

"""Returns a pair. The first is the row given as an answer,
   and the second is a list of 4 lists containing the numbers
   in the matrix.
"""
def ReadCase(input_file):
  answer = int(input_file.readline()) - 1
  matrix = []
  for x in range(4):
    line = input_file.readline()
    line = line.split()
    matrix.append(line)

  return (answer, matrix)

def SolveCase(input_file):
  first,first_matrix = ReadCase(input_file)
  second,second_matrix = ReadCase(input_file)

  first_set = set(first_matrix[first])
  second_set = set(second_matrix[second])

  print 'First set: ',
  print first_set
  print 'Second set: ',
  print second_set

  intersection = first_set.intersection(second_set)
  if len(intersection) == 0:
    return 'Volunteer cheated!'
  elif len(intersection) > 1:
    return 'Bad magician!'
  else:
    return intersection.pop()

def main(argv):
  solution_file_name = 'solution_' + argv[0]
  cases = open(argv[0], 'r')
  num_cases = int(cases.readline())
  
  answers = []
  for i in range(num_cases):
    answers.append(SolveCase(cases))

  # Print the answers to file
  solution = open(solution_file_name, 'w')
  for counter in range(num_cases):
    sol = 'Case #%d: %s\n'%(counter+1, answers[counter])
    solution.write(sol)

  solution.close()

if __name__ == '__main__':
  main(sys.argv[1:])
