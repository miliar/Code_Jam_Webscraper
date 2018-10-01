# Qualification Round Problem A

i = open("A-large.in", "r")
o = open("A-large.out", "w")

T = int(i.readline())

Xs = ["XXXX", "XXXT", "XXTX", "XTXX", "TXXX"]
Os = ["OOOO", "OOOT", "OOTO", "OTOO", "TOOO"]

for c in range(1, T + 1):
  board = []
  for p in range(4):
    line = i.readline().replace('\n','')
    board.append(line)

  emptyline = i.readline()
  decided = False

  # Horizontal
  for line in board:
    if line in Xs:
      result = "X won"
      decided = True
      break
    if line in Os:
      result = "O won"
      decided = True
      break

  # Diagonals
  if not decided:
    diag1, diag2 = [],[]
    for x in range(4):
      diag1.append(board[x][x])
      diag2.append(board[x][3-x])
        
    # Diagonal 1  
    line = "".join(diag1)
    if line in Xs:
      result = "X won"
      decided = True
    elif line in Os:
      result = "O won"
      decided = True
        
    # Diagonal 2
    if not decided:
      line = "".join(diag2)
      if line in Xs:
        result = "X won"
        decided = True
      elif line in Os:
        result = "O won"
        decided = True


  # Verticals
  if not decided:
    for x in range(4):
      col = []
      for y in range(4):
        col.append(board[y][x])
      line = "".join(col)
      if line in Xs:
        result = "X won"
        decided = True
        break
      elif line in Os:
        result = "O won"
        decided = True
     
  # Stil not decided
  if not decided:
    for line in board:
      if "." in line:
        result = "Game has not completed"
        decided = True
        break

  if decided:
    o.write("Case #{0}: {1}\n".format(c, result))
  else:
    o.write("Case #{0}: {1}\n".format(c, "Draw"))


i.close()
o.close()