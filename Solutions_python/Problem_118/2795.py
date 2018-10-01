import sys
def sqrt(n):
  guesses = set([n])
  x = n//2
  while x*x != n:
    #print("testing", x)
    x = (x + n // x) // 2
    if x in guesses:
      return -1
    guesses.add(x)
  return x

if __name__ == "__main__":
  f = sys.stdin
  if len(sys.argv) >= 2:
    fn = sys.argv[1]
    f = open(fn, 'r')
  cases = int(f.readline())
  for i in range(cases):
    sys.stdout.write ("Case #"+str(i + 1)+": ")
    ln = f.readline()
    ln = ln.split()
    a = int(ln[0])
    lb = a
    b = int(ln[1])
    numf = 0
    """while(a < 100000 and a <= b): 
      if int(str(a)[::-1]) == a:
        sq = sqrt(a)
        if sq>0 and int(str(sq)[::-1]) == sq:
          print(a)
          numf += 1
      a += 1"""
    if a <= b:
      l = len(str(a))
      if l%2 == 0:
        h = str(a)[0:l//2]
      else:
        h = str(a)[0:l//2 + 1]
      while(a <= b):
        a = int("".join(h + h[-2::-1]))
        #print(a)
        if int(str(a)[::-1]) == a and a >= lb and a <= b:
          #print ("INNER LOOP")
          if a == 1:
            numf += 1
          else:
            sq = sqrt(a)
            if sq>0 and int(str(sq)[::-1]) == sq:
              #print(a)
              numf += 1
        h = str(int(h)+1)
    print(numf)

