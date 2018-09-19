n=500

fact = [1]
for i in range(1,n+1):
    fact.append(i*fact[i-1])

npr = []    
for i in range(0,n+1):
  npr.append([])
  for j in range(0,n+1):
    npr[i].append(fact[i]/(fact[j]*fact[i-j]))
    
X = []
N = []
for i in range(0,n+1):
  N.append(0)
  X.append([])
  for j in range(0,n+1):
    X[i].append(0)

for i in range(2,n+1):
  X[i][1] = 1

N[2] = 1

for i in range(3,n+1):
  for j in range(2,i):
    for k in range(1,j):
      X[i][j] += X[j][k]*npr[i-j-1][j-k-1]
  N[i] = sum(X[i])
  
infile = open('C-large.in','r')
outfile = open('C-large.out','w')

T = int(infile.readline().strip('\n'))

for case in range(1,T+1):
  n = int(infile.readline().strip('\n'))
  out = N[n] % 100003
  outfile.write("Case #" + str(case) + ": " + str(out) + "\n")
  
infile.close()
outfile.close()