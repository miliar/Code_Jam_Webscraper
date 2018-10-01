# Google Code Jam 2013
# Problem B. Lawnmower

def solve(board, lawn):
  rows = len(board)
  cols = len(board[0])

  for q in lawn:
    #print q
    f = True
    c = True
    fila = q[1]
    colu = q[2]
    v = q[0]
    for i in range(cols):
      if board[fila][i] > v:
        f = False
    for i in range(rows):
      if board[i][colu] > v:
        c = False
    if (not f) and (not c):
      return False

  return True

cases = int(raw_input())

for cases_r in range(cases):
  (rows, cols) = raw_input().split()

  rows = int(rows)
  cols = int(cols)

  lawn = []
  board = []

  for i in range(rows):
    fila = raw_input().split()
    thisrow = []
    for j in range(cols):
      v = int(fila[j])
      lawn.append((v, i, j))
      thisrow.append(v)
    board.append(thisrow)

  lawn.sort()

  print "Case #%d: %s" %( cases_r + 1, "YES" if solve(board, lawn) else "NO" )


