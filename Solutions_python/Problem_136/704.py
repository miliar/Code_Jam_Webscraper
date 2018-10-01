def base(c, n, i):	
  if i == 0:
    return 0
  else:
    return c/n

def main():
  t = int(input())
  for a in range(t):
    line = input()
    l = line.split()
    l = [ float(fl) for fl in l ]
    c, f, x = l
    i = 0
    time = x
    prev = x + 1
    n = 0
    b = 0
    while time < prev:
      prev = time
      b = b + base(c,n,i)
      n = 2 + (f * i)
      time = b + (x / n)
      i = i + 1
    print("Case #{0}: {1:.7f}".format( a + 1, prev))
  
main()