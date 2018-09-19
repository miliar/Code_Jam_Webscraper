# Problem A - Tic-Tac-Toe-Tomek by enrmarc
import sys 

SYMBOL = 'T'
SIZE   = 4

def check(grid):
   result = False
   completed = True
   player = ''

   # Check horizontal lines
   for i in range(0, SIZE):
     result = all((x == grid[i * SIZE] or x == SYMBOL) for x in grid[i * SIZE:(i * SIZE) + SIZE])
     if result:
        player = grid[i * SIZE]
        return result, player, completed

   # Check vertical lines
   for i in range(0, SIZE):
      result = all((x == grid[i] or x == SYMBOL) for x in grid[i::SIZE])
      if result:
         player = grid[i]
         return result, player, completed

   # Check diagonals
   result = all((x == grid[0] or x == SYMBOL) for x in grid[0::SIZE + 1])
   if result:
      player = grid[0]
      return result, player, completed

   result = all((x == grid[SIZE - 1] or x == SYMBOL) for x in grid[SIZE - 1:(SIZE*SIZE) - SIZE + 1:SIZE - 1])
   if result:
      player = grid[SIZE - 1]
      return result, player, completed

   completed = all(x != '.' for x in grid)

   return False, player, completed

if __name__ == '__main__':
   with sys.stdin as filein:
      lines = [line.rstrip() for line in filein if line.rstrip()]
   cases = int(lines[0])
   lines = lines[1:]
   
   for i in range(cases):
      grid = "".join(lines[i * SIZE:(i * SIZE) + SIZE])
      result, player, completed = check(grid)

      if result and player != '.':
         status = ' won'
      elif player == '.':
         status = 'Game has not completed'
      elif not player:
         status = 'Draw'
      player = player if player != '.' else ''
     
      if not completed: status = 'Game has not completed'

      print 'Case #' + str(i + 1) + ': ' + player + status
