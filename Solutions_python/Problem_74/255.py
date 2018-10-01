#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2011 May  7
import sys
import math

def steps(start_pos, end_pos):
  return math.fabs(end_pos - start_pos)

def other_robot(robot):
  if robot == 'O':
    return 'B'
  if robot == 'B':
    return 'O'

def main():
  file = open(sys.argv[1])

  nb_cases = int(file.readline())

  for case_nb in range(1, nb_cases + 1):
    positions = { 'O': 1, 'B': 1 }
    last_time = 0
    waits = { 'O': 0, 'B' : 0 }
    str = file.readline().replace('\n','')
    tokens = str.split(' ')
    nb_buttons = int(tokens[0])
    t_time = 0
    for button_nb in range(0, nb_buttons):
      robot = tokens[button_nb * 2 + 1]
      button = int(tokens[button_nb * 2 + 2])
      local_time = max(0, steps(positions[robot], button) - waits[robot])
      t_time = t_time + local_time + 1
      waits[robot] = 0
      waits[other_robot(robot)] = waits[other_robot(robot)] + local_time + 1
      positions[robot] = button

    print("Case #%s: " % case_nb + "%s" % int(t_time))

  file.close()

if __name__ == "__main__":
  main()
