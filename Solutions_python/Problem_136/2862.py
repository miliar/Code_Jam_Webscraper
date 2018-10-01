import sys

def readfile():
  try:
    filename = sys.argv[1]
  except:
    print "Use filename as argument"
    sys.exit(1)

  try:
    with open(filename) as f:
      l = [a.strip() for a in f.readlines()]
  except:
    print "Use valid filename as argument"
    sys.exit(1)

  numinputs = int(l.pop(0))
  l = [[float(a) for a in line.split()] for line in l]
  return numinputs, l

def genC(c,f):
  rate = 2
  while True:
    yield c/rate
    rate += f

def genX(x,f):
  rate = 2 + f
  while True:
    yield x/rate
    rate += f

def solve(variables):
  C,F,X = variables
  rate = 2

  gc = genC(C,F)
  gx = genX(X,F)

  min = X/rate
  sum = 0

  for i in xrange(10**5):
    sum += gc.next()
    c = sum + gx.next()
    if c < min:
      min = c
  return min

def main():
  numinputs, inputs = readfile()

  for i in range(numinputs):
    ans = solve(inputs[i])
    print "Case #{0}: {1:.7f}".format(i+1, ans)

if __name__ == "__main__":
  #print solve([246.0, 2.0, 492.0])
  main()
