import sys

input = sys.stdin

def solve(d, p):
    mx = p[0]
    for pc in p:
      if pc>mx:
        mx = pc
    for x in range(mx, 1, -1):
      t = time(x,p)
      mx = min(mx, t)
    return mx

def time(x, p):
  t = 0
  for pc in p:
    if pc > x:
      t = t+ pc//x - (pc%x == 0)
  return t + x    


for case in range(int(input.readline())):
      d = int(input.readline())
      p = [int(i) for i in input.readline().split()]
      print("Case #"+ str(case+1) +":", solve(d, p))
  
