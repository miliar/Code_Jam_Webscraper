import sys

def stripline(): return sys.stdin.readline().rstrip()
def parseline(): return stripline().split(" ")

def isvalid(a,b,c):
  x = a[0]+b[0]+c[0]
  y = a[1]+b[1]+c[1]
  if x%3 == 0 and y%3 == 0: return True
  return False

N = int(parseline()[0])
for j in range(N):
  input = parseline()
  (n,A,B,C,D,x0,y0,M) = (int(input[0]),int(input[1]),int(input[2]),int(input[3]),int(input[4]),int(input[5]),int(input[6]),int(input[7]))
  
  list = []
  X = x0; Y = y0
  list.append((X,Y))
#  print X,Y
  for i in range(n-1):
    X = (A*X+B)%M
    Y = (C*Y+D)%M
    list.append((X,Y))
#    print X,Y

  valid = 0
  for i in range(len(list)):
    for k in range(i+1,len(list)):
      for m in range(k+1,len(list)):
        if isvalid(list[i],list[k],list[m]):
          valid += 1
  
  print "Case #"+str(j+1)+": "+str(valid)
