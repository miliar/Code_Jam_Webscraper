
def getNextAndCost(key, cap):
  grps = [long(x) for x in key.split()]
  
  i = 0
  sum = 0
  for g in grps:
    if sum + g > cap:
      break
    else :
      sum = sum + g
      i = i + 1
  
  ride = grps[0:i]
  del grps[0:i]
  grps = grps + ride

  key = ' '.join([str(x) for x in grps])
  
  return key, sum
  

f = open("C-small-attempt1.in")

cases = long(f.readline())
caseno = 0
for x in range(cases):
  dic = {}
  sum = 0 
  rounds,cap,gSize = f.readline().split()
  
  key = f.readline()
  grps = [long(x) for x in key.split()]
  key = ' '.join([str(x) for x in grps])
  
  for i in range(int(rounds)): 
    if key in dic:
      (next, cost) = dic[key]
    else:
      next, cost = getNextAndCost(key, long(cap))
      dic[key] = (next, cost)
  
  #  print "values ", key, next
    sum = sum  + cost
    key = next
  caseno = caseno + 1
  
  print 'Case #%d: %d' % (caseno, sum)
  
  
  
  
  
  
  
