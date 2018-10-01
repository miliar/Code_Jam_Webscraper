import sys

input = sys.stdin

def solve(x,r,c):
  if (r*c)%x != 0:
    return "RICHARD"
  elif x > 7:
    return "RICHARD"
  elif x == 6 and (r< 4 or c < 4):
    return "RICHARD"
  elif x == 5 and (r< 3 or c < 3):
    return "RICHARD"
  elif x == 5 and r==3 and c== 5:
    return "RICHARD"
  elif x == 5 and r==5 and c==3:
    return "RICHARD"
  elif x == 4 and (r< 3 or c < 3):
    return "RICHARD"
  elif x == 3 and (r< 2 or c < 2):
    return "RICHARD"
  elif x == 6 and (r< 6 and c < 6):
    return "RICHARD"
  elif x == 5 and (r< 5 and c < 5):
    return "RICHARD"
  elif x == 4 and (r< 4 and c < 4):
    return "RICHARD"
  elif x == 3 and (r< 3 and c < 3):
    return "RICHARD"
  else:
    return "GABRIEL"
    


for case in range(int(input.readline())):
      values = [int(i) for i in input.readline().split()]
      print("Case #"+ str(case+1) +": "+solve(values[0], values[1], values[2]))
  
