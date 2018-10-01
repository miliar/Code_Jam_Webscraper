import math

def ispal(x):
  return str(x)[::-1] == str(x)

def main():
  nc = int(input())
  for i in range(nc):
    count = 0
    a,b = [int(x) for x in raw_input().split()]

    # firstly, only need to consider squares.
    first = math.ceil(a**0.5)
    last = math.floor(b**0.5)
    for j in range(first, last + 1):
      if ispal(j) and ispal(j**2):
        count += 1

    print 'Case #%s: %s' % (i + 1, count )
main()