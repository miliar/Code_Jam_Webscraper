moves = 0
pancakes = []
import sys
sys.setrecursionlimit(1500)

def allHappy():
  for p in pancakes:
    if p == False:
      return False
  return True
  
def change(pos, k):
  global moves
  
  if allHappy():
    return
    
  moves += 1
  
  while pancakes[pos] and pos + k < len(pancakes):
    pos += 1
  
  if pos + k == len(pancakes):
    for i in range(pos, pos + k):
      pancakes[i] = not(pancakes[i])
    return
  
  for i in range(pos, pos + k):
    pancakes[i] = not(pancakes[i])
    
  change(pos, k)
  
  

n = int(input())
for case in range(1, n+1):
  cit = str(input())
  cit = cit.split()
  
  k = int(cit[1])
  
  pancakes = []
  moves = 0
  
  for c in cit[0]:
    pancakes.append( c == "+" )
    
  if allHappy():
    print("Case #" + str(case) + ": 0")
  else:
    change(0, k)
    if allHappy():
      print("Case #" + str(case) + ": " + str(moves) + "")
    else:
      print("Case #" + str(case) + ": IMPOSSIBLE")