
import sys
from array import *


winners_horizontal_O = [['O', 'O', 'O', 'O'], ['O', 'O', 'O', 'T'], ['O', 'O', 'T', 'O'], ['O', 'T', 'O', 'O'], ['T', 'O', 'O', 'O']]
winners_horizontal_X = [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'T'], ['X', 'X', 'T', 'X'], ['X', 'T', 'X', 'X'], ['T', 'X', 'X', 'X']]

def launch_error(text_error):
  raise Exception(text_error);

def get_matches(file_path):
  file = open(file_path)
  n_matches = file.readline()
  matches = []

  single_match = []

  i = 0
  for row in file.readlines():
    if i < 4:
      char_row = []
      line = row.split("\n")[0]
      for char in line:
        char_row.append(char)
      single_match.append(char_row)
      i += 1
    else:
      matches.append(single_match)
      single_match = []
      i = 0
  matches.append(single_match)

  file.close()

  return (n_matches, matches)

def chk_horizontal_O(row):
  for check in winners_horizontal_O:
    if check == row:
      return True
  return False

def chk_horizontal_X(row):
  for check in winners_horizontal_X:
    if check == row:
      return True
  return False

def bsc_check(char, cmp):
  if char == cmp or char == 'T':
    return True
  else:
    return False

def chk_vertical(match):
  for col in range(0, 4):
    if bsc_check(match[0][col], 'X') and bsc_check(match[1][col], 'X') and bsc_check(match[2][col], 'X') and bsc_check(match[3][col], 'X'):
      return 'X'
    if bsc_check(match[0][col], 'O') and bsc_check(match[1][col], 'O') and bsc_check(match[2][col], 'O') and bsc_check(match[3][col], 'O'):
      return 'O'
  return 'T'

def chk_diagonal(match):
  if bsc_check(match[0][0], 'X') and bsc_check(match[1][1], 'X') and bsc_check(match[2][2], 'X') and bsc_check(match[3][3], 'X'):
    return 'X'
  if bsc_check(match[0][0], 'O') and bsc_check(match[1][1], 'O') and bsc_check(match[2][2], 'O') and bsc_check(match[3][3], 'O'):
    return 'O'
  if bsc_check(match[0][3], 'X') and bsc_check(match[1][2], 'X') and bsc_check(match[2][1], 'X') and bsc_check(match[3][0], 'X'):
    return 'X'
  if bsc_check(match[0][3], 'O') and bsc_check(match[1][2], 'O') and bsc_check(match[2][1], 'O') and bsc_check(match[3][0], 'O'):
    return 'O'
  return 'T'

def chk_no_finished(match):
  for row in match:
    for char in row:
      if char == '.':
        return 'N'
  return 'T'

def check_match(match):
  for row in match:
    if chk_horizontal_O(row):
      return 'O'
    if chk_horizontal_X(row):
      return 'X'
  result = chk_vertical(match)
  if result == 'T':
    result = chk_diagonal(match)
    if result == 'T':
      result = chk_no_finished(match)
  return result;


if __name__ == '__main__':
  if (len(sys.argv) == 2):
    file_path = sys.argv[1]
  else:
    launch_error("Needs input file")

  (n_matches, matches) = get_matches(file_path)

  i = 1
  for match in matches:
    m_status = check_match(match)
    if m_status == 'O':
      print "Case #" + str(i) + ": O won"
    elif m_status == 'X':
      print "Case #" + str(i) + ": X won"
    elif m_status == 'T':
      print "Case #" + str(i) + ": Draw"
    elif m_status == 'N':
      print "Case #" + str(i) + ": Game has not completed"
    else:
      print "Case #" + str(i) + ": Error"

    i += 1
  
