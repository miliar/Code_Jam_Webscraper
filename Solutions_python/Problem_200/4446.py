
def intToDigits(n):
  return [int(i) for i in str(n)]



def findTidy(n):
  l = intToDigits(n)
  untidy = True
  while untidy:
    untidy = False
    for i in range(len(l)-1):
      if l[i] > l[i+1]:
        l[i] -= 1
        l[i+1] = 9
        for k in range(i+1, len(l)): # make the right side 9
          l[k] = 9
        untidy = True
        break
        
  return int( ''.join(str(x) for x in l) )


output = []
total = int(input())
while total > 0:
  total -= 1
  n = int(input())
  output.append( findTidy(n) ) 

for i,n in enumerate(output):
  print("Case #{}: {}".format(i+1, n))






def isTidy2(n):
  #print("isTidy({})".format(n))
  tidy = False
  rDigit = n%10
  t = n//10
  while t:
    lDigit = t%10
    #print("lDigit {}, rDigit {}, t {}".format(lDigit,rDigit, t))
    if lDigit > rDigit:
      return False
    rDigit = lDigit
    t //= 10
  
  return True


def getDigits2(n):
  l = []
  while n:
    l.append(n%10)
    n //= 10
  l.reverse()
  return l



def isTidy2(n):
  l = getDigits(n)
  #print("isTidy({}), digits: {}".format(n, l))
  prev = l[0]
  for x in l:
    if x < prev:
      return False
    prev = x
  return True



def findTidy2(t):
  while t > 9:
    if isTidy(t):
      break
    t -= 1
  return t



