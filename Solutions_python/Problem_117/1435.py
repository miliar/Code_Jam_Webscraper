f=open("B-large.in","r")
g=open("mow.out","w")

T = int(f.readline())

for i in range(0,T):
  W = []
  F = []
  C = []
  X = f.readline().split( )
  N = int(X[0])
  M = int(X[1])
  K = 0
  
  for l in range(0,N):
    A = map(int,f.readline().split( ))
    F.append(max(A))
    W.append(A)
    
  for j in range(0,M):
    I = [L[j] for L in W]
    C.append(max(I))
  
  
  for x in range(0,M):
    for y in range(0,N):
      if W[y][x] == F[y] or W[y][x] == C[x]:
        K += 1
      else:
        break
  
  if K == M*N:
    R = 'YES'
  else:
    R = 'NO'

  g.write("Case #"+str(i+1)+": "+R+"\n")

