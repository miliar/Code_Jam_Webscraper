
import sys

f = open('C-small-attempt0.in', 'r')
outfile = open('C-small-attempt0.out', 'w')

N = f.readline()

def countcoins(l, n):
  count = 0
  l[n] = 0
  
  for i in range(n+1 , len(l)):
    if (l[i] == 0):
      break
    count = count +1

  for i in range(1, n)[::-1]:
    if (l[i] == 0):
      break
    count = count +1
  return (l, count)
    
def cells(P):
  list1 = [0]
  for i in range(0, P):
    list1 = list1 + [1]
  list1 = list1 + [0]
  return list1

def perms(str):
    if len(str) <=1:
        yield str
    else:
        for p in perms(str[1:]):
            for i in range(len(p)+1):
                yield p[:i] + str[0:1] + p[i:]

def count(cel, p):
  total = 0
  for i in p:
    cel, c = countcoins(cel, i)
    total = total + c
  return total

def calculate(Q, P, freelist):
  cel = cells (P)
  newcel = cells (P)
  min = sys.maxint
  
  for  p in perms(freelist):
    cel = cells (P)
    c = count(cel, p)
    if (min > c):
      min  = c
  return min


for i in range(1, int(N)+1):
  P, Q = f.readline().strip().split()
  Q = int(Q)
  P = int(P)
  l = f.readline().strip().split()
  l = map(lambda x: int(x), l)
  
  
  outfile.write("Case #" + str(i) + ": "+ str(calculate(Q, P, l)) + "\n" )
  print ("Case #" + str(i) + ": "+ str(calculate(Q, P, l)) + "\n" )

outfile.close()
