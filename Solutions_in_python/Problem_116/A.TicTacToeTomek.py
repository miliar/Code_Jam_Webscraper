PLAYERS = ['X', 'O']
WINNER = [False, False]
board = []
fout = open('A-large.out', 'w')

def resetTest():
  global board, WINNER
  board = []
  WINNER = [False, False]

def owns(player, i, j):
  return board[i][j] == player or board[i][j] == 'T'

def checkForWinner(p, ownedTiles):
  if ownedTiles == 4:
    WINNER[p] = True

def write(s):
  global fout
  fout.write(s)

def printWinner():
  if WINNER[0] and not WINNER[1]:
    write(PLAYERS[0] + ' won\n')
  elif not WINNER[0] and WINNER[1]:
    write(PLAYERS[1] + ' won\n')
  else:
    # Check for incomplete board.
    incomplete = False
    for i in range(4):
      for j in range(4):
        if board[i][j] == '.':
          incomplete = True
    if incomplete:
      write('Game has not completed\n')
    else:
      write('Draw\n')

def run(filename):
  global board, WINNER
  f = open(filename)
  numTests = int(f.readline().strip());

  for test in range(numTests):
    write('Case #' + str(test + 1) + ': ')

    # Read in the board.
    resetTest()
    for i in range(4):
      row = []
      line = f.readline().strip()
      for j in range(4):
        row.append(line[j])
      board.append(row)
  
    # Figure out board status.

    # Check downward diagonal.
    for p, player in enumerate(PLAYERS):
      ownedTiles = 0
      for i in range(4):
        if owns(player, i, i):
          ownedTiles += 1
        else:
          break
      checkForWinner(p, ownedTiles)

    # Check upward diagonal.
    for p, player in enumerate(PLAYERS):
      if WINNER[p]:
        break
      ownedTiles = 0
      for i in range(4):
        if owns(player, 3 - i, i):
          ownedTiles += 1
        else:
          break
      checkForWinner(p, ownedTiles)

    # Check horizontals.
    for p, player in enumerate(PLAYERS):
      if WINNER[p]:
        break
      for i in range(4):
        ownedTiles = 0
        for j in range(4):
          if owns(player, i, j):
            ownedTiles += 1
          else:
            break
        checkForWinner(p, ownedTiles)

    # Check verticals.
    for p, player in enumerate(PLAYERS):
      if WINNER[p]:
        break
      for i in range(4):
        ownedTiles = 0
        for j in range(4):
          if owns(player, j, i):
            ownedTiles += 1
          else:
            break
        checkForWinner(p, ownedTiles)

    printWinner()
    # Skip the empty row between test cases.
    f.readline()

  f.close();

if __name__ == '__main__':
  run('A-large.in')