def isWrong(x):
  for i in range(len(x)-1,0,-1):
    if x[i]<x[i-1]:
      return i-1
  return -1
def normalize(x,pos):
  x[pos]=chr(ord(x[pos])-1)
  for i in range(pos+1,len(x)):
    x[i]='9'
t=int(input())
for testcase in range(0,t):
  n=list(input())
  while isWrong(n)>-1:
    wrongPos=isWrong(n)
    normalize(n,wrongPos)
  result=str(int("".join(n)))
  print("Case #"+str(testcase+1)+": "+result)
  
  