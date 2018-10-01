'''
 Codejam

 Problem 1: The magic trick

 @author Aaron Fas <yo@aaron.com.es>
'''

import sys
from sets import Set

def solve(first, second, game):
  matching = first & second
  amount = len(matching)
  if amount == 1:
    print "Case #{}: {}".format(game, matching.pop())
  elif amount > 1:
    print "Case #{}: Bad magician!".format(game)
  else:
      print "Case #{}: Volunteer cheated!".format(game)

combinations = int(sys.stdin.readline()) * 2

last = None

for game in range(1, combinations+1):
  choice = int(sys.stdin.readline())
  for i in range(1, choice):
    sys.stdin.readline() # Skiplines
  chosen = Set(sys.stdin.readline().strip().split(' '))
  if last == None:
    last = chosen
  else:
    solve(last, chosen, game/2)
    last = None
  for i in range(choice+1, 5):
    sys.stdin.readline() # Skiplines

