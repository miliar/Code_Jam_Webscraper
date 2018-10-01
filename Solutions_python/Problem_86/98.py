import sys
import functools
def toInt(x):
  return int(x)

def new_matrix(L,C,num):
  return [[num for row in range(C)] for col in range(L)] #@UnusedVariable

file = open('mandar.txt','w')
sys.stdout = file

input  = open('a.in')
CASES  = int(input.readline())
for case in range(CASES):
  args = map(toInt,input.readline().strip().split(' '))
  L=args[1]
  H=args[2]
  fs = map(toInt,input.readline().strip().split(' '))
  
  res=None
  for jf in range(L,H+1):
    ok = True
    for f in fs:
      if jf>=f:
        if jf%f!=0:
          ok=False
          break
      else:
        if f%jf!=0:
          ok=False
          break
    if ok:
      res=jf
      break
  ans = res and str(res) or 'NO'
  print 'Case #'+str(case+1)+': '+ans
    
        
      
   
