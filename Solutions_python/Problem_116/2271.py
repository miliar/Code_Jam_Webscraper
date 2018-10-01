#!/usr/bin/python2

import operator
import math

inFile = open ("A-large.in", "r")
outFile = open ("outputs.out", "w")
empty_flag = False

def main ():
  
  global empty_flag
  global inFile
  global outFile
  
  numOfCases = int (inFile.readline())
  for i in range (0, numOfCases):
    empty_flag = False
    X_WIN = False
    O_WIN = False
    main_lst = []
    # Read single test case
    for j in range (0, 4):
      line = inFile.readline ()
      lst = []
      for x in range (0, len (line) - 1):
        lst.append (line[x])
      main_lst.append (lst)
    
    X_WIN = compute (main_lst, 'X')
    if X_WIN == False:
      O_WIN = compute (main_lst, 'O')
    # If empty slots and non won
    if X_WIN == False and O_WIN == False:
      if empty_flag is True:
        outFile.write ("Case #" + str (i + 1) + ": " + "Game has not completed\n")
      else:
        outFile.write ("Case #" + str (i + 1) + ": " + "Draw\n")
    elif X_WIN == True:
      outFile.write ("Case #" + str (i + 1) + ": " + "X won\n")
    elif O_WIN == True:
      outFile.write ("Case #" + str (i + 1) + ": " + "O won\n")
    # Read empty line  
    inFile.readline ()
         
  outFile.close ()
  inFile.close ()

def compute (main_lst, sym):
  global empty_flag
  # Check four rows
  if (check_row (main_lst, sym, 0) == True) \
    or (check_row (main_lst, sym, 1) == True) \
    or (check_row (main_lst, sym, 2) == True) \
    or (check_row (main_lst, sym, 3) == True):
    return True
  # Check four columns
  if (check_col (main_lst, sym, 0) == True) \
    or (check_col (main_lst, sym, 1) == True) \
    or (check_col (main_lst, sym, 2) == True) \
    or (check_col (main_lst, sym, 3) == True):
    return True
  
  # Check two diagonals
  if (main_lst[0][0] == sym or main_lst[0][0] == 'T') \
    and (main_lst[1][1] == sym or main_lst[1][1] == 'T') \
    and (main_lst[2][2] == sym or main_lst[2][2] == 'T') \
    and (main_lst[3][3] == sym or main_lst[3][3] == 'T'):
    return True
  
  if (main_lst[0][3] == sym or main_lst[0][3] == 'T') \
    and (main_lst[1][2] == sym or main_lst[1][2] == 'T') \
    and (main_lst[2][1] == sym or main_lst[2][1] == 'T') \
    and (main_lst[3][0] == sym or main_lst[3][0] == 'T'):
    return True
  
  return False

def check_row (main_lst, sym, row_id):
  
  global empty_flag
  
  if (main_lst[row_id][0] == sym or main_lst[row_id][0] == 'T') \
    and (main_lst[row_id][1] == sym or main_lst[row_id][1] == 'T') \
    and (main_lst[row_id][2] == sym or main_lst[row_id][2] == 'T') \
    and (main_lst[row_id][3] == sym or main_lst[row_id][3] == 'T'):
    return True
  # Check empty slots
  elif empty_flag == False:
    if (main_lst[row_id][0] == '.') or (main_lst[row_id][1] == '.') \
      or (main_lst[row_id][2] == '.') or (main_lst[row_id][3] == '.'):
      empty_flag = True 
      
  return False

def check_col (main_lst, sym, col_id):
  global empty_flag
  
  if (main_lst[0][col_id] == sym or main_lst[0][col_id] == 'T') \
    and (main_lst[1][col_id] == sym or main_lst[1][col_id] == 'T') \
    and (main_lst[2][col_id] == sym or main_lst[2][col_id] == 'T') \
    and (main_lst[3][col_id] == sym or main_lst[3][col_id] == 'T'):
    return True
      
  return False

main ()

