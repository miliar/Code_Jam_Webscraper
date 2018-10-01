import sys

def ReadInts():
  line = sys.stdin.readline().rstrip("\n")
  return map(int, line.split())

def solve(A,N,motes):
  motes.sort()
  current = A
  count = 0
  for i in xrange(N):
    if current > motes[i]:
      current += motes[i]
    else:
      max_count = N-i
      cond = True
      for m in xrange(1,max_count+1):
        current = 2*current - 1
        if current > motes[i]:
          current += motes[i]
          count += m
          cond = False
          break
      if cond:
        return (count + max_count)
  return count

if __name__ == "__main__":
  T = ReadInts()[0]

  for prob in xrange(1,T+1):
    A,N = ReadInts()
    motes = ReadInts()
#      print A,N,motes
    ans = solve(A,N,motes)
    print "Case #%d: %d"%(prob, ans)

  
