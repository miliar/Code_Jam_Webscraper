# -*- coding: utf-8 -*-
import sys

def readgame():
  game = ""
  for i in xrange(4):
    line = sys.stdin.readline().rstrip("\n")
    game += line
  sys.stdin.readline()
  return game

def isConstructedWith(target,elements):
  for e in target:
    if not e in elements:
      return False
  return True

def solve(game):
  for row in xrange(4):
    if isConstructedWith(game[4*row:4*row+4],["O","T"]):
      return "O won"
    if isConstructedWith(game[4*row:4*row+4],["X","T"]):
      return "X won"
  for col in xrange(4):
    if isConstructedWith(game[col]+game[col+4]+game[col+8]+game[col+12],["O","T"]):
      return "O won"
    if isConstructedWith(game[col]+game[col+4]+game[col+8]+game[col+12],["X","T"]):
      return "X won"
  if isConstructedWith(game[0]+game[5]+game[10]+game[15],["O","T"]):
    return "O won"
  if isConstructedWith(game[0]+game[5]+game[10]+game[15],["X","T"]):
    return "X won"
  if isConstructedWith(game[3]+game[6]+game[9]+game[12],["O","T"]):
    return "O won"
  if isConstructedWith(game[3]+game[6]+game[9]+game[12],["X","T"]):  
    return "X won"
  if isConstructedWith(game,["X","O","T"]):
    return "Draw"
  else:
    return "Game has not completed"

if __name__ == "__main__":
  T = int(sys.stdin.readline().rstrip("\n"))
  for t in xrange(1,T+1):
    game = readgame()
    print "Case #%d: %s"%(t,solve(game))
  
