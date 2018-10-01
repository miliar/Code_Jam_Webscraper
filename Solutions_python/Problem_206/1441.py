def Solve(D, N, KS):
  t = []
  for i in KS:
    t.append((D-i[0])/float(i[1]))
  #if float(max(t)) == 0:
  #  print D, N, KS, t
  return '{0:.6f}'.format(D/float(max(t)))


T = int(input())  
for i in range(1, T + 1):
  D, N = [long(s) for s in raw_input().split(" ")]
  KS = []
  for j in range(N):
    KS.append([long(s) for s in raw_input().split(" ")])
  print("Case #{}: {}".format(i,Solve(D, N, KS)))
