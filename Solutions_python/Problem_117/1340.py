#!/usr/bin/env python
import sys
import itertools

def min_singleton_row(board, minel):
  N = len(board)
  singleton_rows = []
  for i in range(N):
    element_set = set(board[i])
    if len(element_set) == 1 and minel in element_set:
      return i
  return None

def min_singleton_col(board, minel):
  N = len(board)
  if N == 0: return None
  M = len(board[0])
  singleton_cols = []
  for i in range(M):
    element_set = set(board[j][i] for j in range(N))
    if len(element_set) == 1 and minel in element_set:
      return i
  return None

def delete_row(board, index):
  board.pop(index)

def delete_col(board, index):
  for i in range(len(board)):
    board[i].pop(index)

def numel(board):
  return sum(len(x) for x in board)

def solve(board):
  while True:
    els = list(itertools.chain(*board))
    if len(els) == 0: return "YES"
    minel = min(els)

    row_min = min_singleton_row(board, minel)
    if row_min is not None:
      delete_row(board, row_min)
      continue

    col_min = min_singleton_col(board, minel)
    if col_min is not None:
      delete_col(board, col_min)
      continue
    return "NO"

T = int(sys.stdin.readline())

for i in range(T):
  N, M = map(int, sys.stdin.readline().strip().split())
  board = []
  for j in range(N):
    board.append([int(x) for x in sys.stdin.readline().strip().split()])

  print "Case #%d: %s" % (i + 1, solve(board))
