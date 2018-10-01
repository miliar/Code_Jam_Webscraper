import collections
from collections import Counter
import pdb
import sys

def readBoard(f):
  return f.readline().strip()\
    + f.readline().strip()\
    + f.readline().strip()\
    + f.readline().strip()

def isFinished(b):
  return b.find('.') == -1

def getLocations(b):
  X = []
  O = []
  for pos,c in enumerate(b):
    if c in ('X', 'T'):
      # (column, row)
      X.append((pos % 4, pos / 4))
    if c in ('O', 'T'):
      O.append((pos % 4, pos / 4))
  return (X,O)

def rowColWin(P):
  ccol = Counter([i for i,j in P])
  crow = Counter([j for i,j in P])
  print >> sys.stderr, "ccol.most_common " + str(ccol.most_common(1))
  print >> sys.stderr, "crow.most_common " + str(crow.most_common(1))
  return ccol.most_common(1)[0][1] > 3 or crow.most_common(1)[0][1] > 3


def diagWin(P):
  # Only two possible options
  return (0,0) in P and (1,1) in P and (2,2) in P and (3,3) in P\
    or (3,0) in P and (2,1) in P and (1,2) in P and (0,3) in P


if __name__ == '__main__':
  import sys
  import pdb
  
  f = open(sys.argv[1], 'r')

  test_cases = int(f.readline())
  for i in range(test_cases):
    board = readBoard(f)
    f.readline() # Read extra line
    print >> sys.stderr, board

    
    (Xs, Os) = getLocations(board)
    print >> sys.stderr, Xs
    print >> sys.stderr, Os
    if 'X' not in board or 'O' not in board:
      xwin = False
      owin = False
    else:
      xwin = rowColWin(Xs) or diagWin(Xs)
      owin = rowColWin(Os) or diagWin(Os)

    if xwin:
      msg = 'X won'
    elif owin:
      msg = 'O won'
    elif isFinished(board):
      msg = 'Draw'
    else:
      msg = 'Game has not completed'

    print 'Case #%d: %s' % ((i+1), msg)
  f.close()
