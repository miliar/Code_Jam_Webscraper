import math
f = open('fair', 'r')
lines = f.readlines()
cases = lines[0]
cases = int(cases[:-1])
init=1
for i in range(cases):
  min=int(lines[init].split(' ')[0])
  max=int(lines[init].split(' ')[1])
#Find squares inside range
    
  low = int(math.ceil(math.sqrt(min)))
  high = int(math.sqrt(max))
  squares=[]
  parts=1
  for p in range(parts):
    for k in range(low, int((p+1)*(high+1)/parts)):
      #purge non-palindromes
      if str(k) == str(k)[::-1]:
        b = k**2
        if str(b) == str(b)[::-1]:
          squares.append(b)
  print 'Case #'+str(i+1)+': '+str(len(squares)) 


  init=init+1
