#! /usr/bin/python3

# Glen Robertson
# Tic-Tac-Toe-Tomek
# Code Jam Qualification Round 2013

def isWonByX(line):
  return line.count('X') + line.count('T') == 4
  
def isWonByO(line):
  return line.count('O') + line.count('T') == 4

numCases = int(input().strip())
for case in range(numCases):
  board = ''
  for i in range(4):
    board += input().strip()
  
  wonByX = False
  wonByO = False
  for i in range(4):
    row = board[4*i:4*(i+1)]
    wonByX |= isWonByX(row)
    wonByO |= isWonByO(row)
    col = board[i::4]
    wonByX |= isWonByX(col)
    wonByO |= isWonByO(col)
  diag1 = board[0] + board[5] + board[10] + board[15]
  diag2 = board[3] + board[6] + board[9] + board[12]
  wonByX |= isWonByX(diag1)
  wonByX |= isWonByX(diag2)
  wonByO |= isWonByO(diag1)
  wonByO |= isWonByO(diag2)
  
  status = ''
  if wonByX:
    status = 'X won'
  elif wonByO:
    status = 'O won'
  elif board.count('.') == 0:
    status = 'Draw'
  else:
    status = 'Game has not completed'
    
  print('Case #' + str(case+1) + ':', status)
  
  
  try:
    input() # Empty line
  except EOFError:
    pass
    