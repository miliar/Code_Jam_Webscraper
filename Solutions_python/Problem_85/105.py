import sys
import functools
def toInt(x):
  return int(x)

def new_matrix(L,C,num):
  return [[num for row in range(C)] for col in range(L)] #@UnusedVariable
sys.setrecursionlimit(10000)
file = open('mandar.txt','w')
sys.stdout = file

def get_dist(index):
  return a[index%len(a)]
a=[]
t=0
def solve(table,N,L):
  if N==0:
    return 0
  if not table[N][L]:
    val1 = solve(table,N-1,L)+get_dist(N-1)*2
    timeBefore = L>0 and solve(table,N-1,L-1) or solve(table,N-1,L)
    timeToComplete = (t-timeBefore>0) and (t-timeBefore) or 0
    val2=get_dist(N-1)*2
    if val2>timeToComplete and L>0:
      val2 = timeToComplete/2 +get_dist(N-1)
    val2=val2+timeBefore
    table[N][L] = min([val1,val2])
  return table[N][L]

input  = open('a.in')
CASES  = int(input.readline())
for case in range(CASES):
  args = map(toInt,input.readline().split(' '))
  L = args[0]
  t = args[1]
  N = args[2]
  C = args[3]
  a=[]
  for i in range(C):
    a.append(args[4+i])
  table = new_matrix(N+1, L+1, 0)
  res = [solve(table,N,n) for n in range(L+1)]
  res = min(res)
#  res = solve(table,N,L)
  print 'Case #'+str(case+1)+': '+str(res)
    
        
      
   
