#!/usr/bin/python
import sys

codeset = [15, 240, 3840, 61440, 4369, 8738, 17476, 34952, 33825, 4680]
def checkboard(board):
  codeX = 0
  codeO = 0
  for i in range(16):
    if board[i] == 'T':
      codeX = codeX | (1<<i)
      codeO = codeO | (1<<i)
    elif board[i] == 'O':
      codeO = codeO | (1<<i)
    elif board[i] == 'X':
      codeX = codeX | (1<<i)
  #print board, codeX, codeO
  for c in codeset:
    if (c & codeX) == c:
      return 'X won'
    if (c & codeO) == c:
      return 'O won'
  if '.' in board:
    return 'Game has not completed'
  return 'Draw'

def main():
  case = int(sys.stdin.readline())
  for i in range(case):
    board = ''
    for j in range(4):
      board = board + sys.stdin.readline().strip()
    rlt = checkboard(board)
    sys.stdin.readline()
    print 'Case #%d: %s' % (i+1, rlt)

if __name__ == '__main__':
  main()
