#!/usr/bin/python

import sys

num_cases = None 
test_case = 0
current = []

def print_winner(test_case, player):
  print "Case #%d: %s won" % (test_case,player)

def check_candidate(candidate):
  first = candidate[0]
  last = candidate[3]
  player = None
  player_won = False
  if first and last and (first == 'T' or last == 'T' or first == last):
    player = first if first != 'T' else last
    player_won = True
    for x in range(1,3):
      if candidate[x] != 'T' and candidate[x] != player:
        player_won = False
        break

  return player_won, player


def solve(test_case, game):
  # first check rows
  for candidate in current:
    won, player = check_candidate(candidate)
    if won:
      print_winner(test_case, player) 
      return
    
  # second check cols
  for y in range(0,4):
    candidate = []
    for x in range(0,4):
      candidate.append(current[x][y])

    won, player = check_candidate(candidate)
    if won:
      print_winner(test_case, player) 
      return

  # check diagonals
  candidate = [game[0][0], game[1][1], game[2][2], game[3][3]]
  won, player = check_candidate(candidate)
  if won:
    print_winner(test_case, player) 
    return

  # check diagonals
  candidate = [game[0][3], game[1][2], game[2][1], game[3][0]]
  won, player = check_candidate(candidate)
  if won:
    print_winner(test_case, player) 
    return

  # check if draw or in progress
  for i in range(0,3):
    for j in range(0,3):
      if not current[i][j]:
        print "Case #%d: Game has not completed" % test_case
        return

  print "Case #%d: Draw" % test_case


def parse_input_row(row):
  parsed_row = []
  for x in range(0,len(row)):
    if row[x] == '.':
      parsed_row.append(None)
    else:
      parsed_row.append(row[x])

  return parsed_row

for line in sys.stdin:
  cleaned_line = line.strip()
  if len(cleaned_line) != 0:
    if not num_cases:
      num_cases = int(cleaned_line)
    else:
      current.append(parse_input_row(cleaned_line))

    if len(current) == 4:
      test_case+=1
      solve(test_case, current)
      current = []
  else:
    current = []
