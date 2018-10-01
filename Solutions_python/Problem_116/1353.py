#!/usr/bin/env python2

import math

count = int(raw_input())

for x in xrange(1,count+1):
  table = []
  for y in range(0,4):
    row = list(raw_input())
    table.append(row)
  raw_input()

  board_full = True
  winner = 0 # 0 None, 1 X, 2 O
  # Iterate on rows
  for y in xrange(0,4):
    x_count = 0
    o_count = 0
    t_count = 0
    for z in xrange(0,4):
      item = table[y][z]
      if item == "X":
        x_count += 1
      elif item == "O":
        o_count += 1
      elif item == ".":
        board_full = False
      else:
        t_count += 1
    if t_count >= 1:
      if x_count == 3:
        winner = 1
        break
      elif o_count == 3:
        winner = 2
        break
    elif x_count == 4:
      winner = 1
      break
    elif o_count == 4:
      winner = 2
      break
  if winner == 0:
    # Iterate on cols
    for y in xrange(0,4):
      x_count = 0
      o_count = 0
      t_count = 0
      for z in xrange(0,4):
        item = table[z][y]
        if item == "X":
          x_count += 1
        elif item == "O":
          o_count += 1
        elif item == ".":
          board_full = False
        else:
          t_count += 1
      if t_count >= 1:
        if x_count == 3:
          winner = 1
          break
        elif o_count == 3:
          winner = 2
          break
      elif x_count == 4:
        winner = 1
        break
      elif o_count == 4:
        winner = 2
        break
  if winner == 0:
    # Iterate on diagonals
    for y in xrange(0,2,1):
      x_count = 0
      o_count = 0
      t_count = 0
      for z in xrange(0,4):
        item = table[z][y*3 + z - 2*y*z]
        if item == "X":
          x_count += 1
        elif item == "O":
          o_count += 1
        elif item == ".":
          board_full = False
        else:
          t_count += 1
      if t_count >= 1:
        if x_count == 3:
          winner = 1
          break
        elif o_count == 3:
          winner = 2
          break
      elif x_count == 4:
        winner = 1
        break
      elif o_count == 4:
        winner = 2
        break

  if winner == 1:
    result = "X won"
  elif winner == 2:
    result = "O won"
  elif winner == 0 and board_full:
    result = "Draw"
  else:
    result = "Game has not completed"
  print "Case #" + str(x) + ": " + result
