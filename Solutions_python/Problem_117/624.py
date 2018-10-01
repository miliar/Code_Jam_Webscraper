#!/usr/bin/python
  
def solve():
  [N,M] = map(int, f.pop(0).split())
  P = []
  for n in range(N):
    P += [f.pop(0).split()]
  if N==1 or M==1: return "YES" 
  h = [P[n] for n in range(N)]
  v = [[P[n][m] for n in range(N)] for m in range(M)]
  hmax=map(max,h)
  vmax=map(max,v)
  for n in range(N):
    for m in range(M):
      o = P[n][m]
      if o<hmax[n] and o<vmax[m]: return "NO"
  else: return "YES"   
  
infile=open("B-small-attempt1.in",'r')
f=map(lambda s:s.strip(),infile.readlines())
infile.close()
N = int(f.pop(0))
out=open("B-small-result",'w')
for n in range(N):
  out.write("Case #%s: %s\n"%(n+1, solve()))
out.close()