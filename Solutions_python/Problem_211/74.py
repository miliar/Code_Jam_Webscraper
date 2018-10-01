def prod(lst):
  x = 1.0
  for y in lst:
    x *= y
  return x

def solve(N,K,U,P):
  sortP = sorted(P)
  while(U > 0):
    minval = sortP[0]
    maxindex = N-1
    for i in xrange(N):
      if sortP[i] > minval:
        maxindex = i-1
        break
    if maxindex == N-1:
      for i in xrange(N):
        sortP[i] += U / N
      return prod(sortP)
    else:
      nextmin = sortP[maxindex+1]
      incamount = min(nextmin - minval, U / (maxindex+1))
      for i in xrange(maxindex+1):
        sortP[i] += incamount
        U -= incamount
        
  return prod(sortP)
        
def floats(lst):
  return [float(x) for x in lst]
      
def main():
  name = "C-small-1-attempt0"
  lines = open(name+'.in').read().split("\n")
  out = []
  num_tests = int(lines[0])
  spot = 1
  for test in xrange(num_tests):
    parts = lines[spot].split(" ")
    N = int(parts[0])
    K = int(parts[1])
    U = float(lines[spot+1])
    P = floats(lines[spot+2].split(" "))
    res = "Case #%d: %.9f" % (test+1, solve(N,K,U,P))
    out.append(res)
    print(res)
    spot += 3

  open(name+'.out','w').write("\n".join(out))
    
main()