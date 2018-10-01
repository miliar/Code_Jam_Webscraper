cases = int(input())

def occupied(stalls, pos):
  if stalls[pos]:
    return (-1, -1)
  
  Ls = 0
  Rs = 0
  
  k = pos
  while(not(stalls[k])):
    k -= 1
    Ls += 1
    
  k = pos
  while(not(stalls[k])):
    k += 1
    Rs += 1
    
  return (Ls-1, Rs-1)

for case in range(1, cases + 1):
  cin = input()
  cin = cin.split()
  
  n = int(cin[0])
  k = int(cin[1])
  
  stalls = [False] * (n + 2)
  stalls[0]     = True
  stalls[n + 1] = True
  
  
  
  for person in range(k):
    maxxy = 0
    posit = 0
    maxLs = 0
    maxRs = 0
    
    found = False
    
    for i in range(1, n + 1):
      (Ls, Rs) = occupied(stalls, i)
      if min(Ls, Rs) > maxxy:
        found = True
        maxxy = min(Ls, Rs)
        maxLs = Ls
        maxRs = Rs
        posit = i
      elif min(Ls, Rs) == maxxy:
        a = max(Ls, Rs)
        b = max(maxLs, maxRs)
        
        if a > b:
          maxxy = min(Ls, Rs)
          maxLs = Ls
          maxRs = Rs
          posit = i
        
    stalls[posit] = True
    if person == k-1:
      print("Case #" + str(case) + ":", max(maxLs, maxRs), min(maxLs, maxRs))