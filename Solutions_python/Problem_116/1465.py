

def check(board, r, c, ri, ci):
  tp = ''
  for i in range(4):
    cur = board[r+i*ri][c+i*ci]
    if cur == 'T' or tp == '' or cur == tp:
      if tp == '' and cur != 'T':
        tp = cur
    else:
      return ''
  return tp

T = int(input())

for t in range(1,T+1):
  board = [['.' for j in range(4)] for i in range(4)]
  for i in range(4):
    line = input()
    for j in range(4):
      board[i][j] = line[j]
  line = input()
  res = ''
  res += check(board, 0, 0, 1, 0)
  res += check(board, 0, 1, 1, 0)
  res += check(board, 0, 2, 1, 0)
  res += check(board, 0, 3, 1, 0)
  
  res += check(board, 0, 0, 0, 1)
  res += check(board, 1, 0, 0, 1)
  res += check(board, 2, 0, 0, 1)
  res += check(board, 3, 0, 0, 1)
  
  res += check(board, 0, 0, 1, 1)
  res += check(board, 3, 0, -1, 1)
  #print(board)
  #print(res)
  if 'X' in res:
    out = 'X won'
  elif 'O' in res:
    out = 'O won'
  elif '.' in board[0]+board[1]+board[2]+board[3]:
    out = 'Game has not completed'
  else:
    out = 'Draw'
  print('Case #' + str(t) + ': ' + out)
