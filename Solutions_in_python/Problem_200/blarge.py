t = int(raw_input())
t+=1
for x in xrange(1,t):
  n = raw_input().strip()
  flag = True
  ctr=0
  l = map(int, n)
  #print l
  siz = len(l)
  prev=l[siz-1]

  ctr=0
  if siz==1:
    y=n
    print "Case #%s: %s"%(x,y)
  else:
    l.reverse()
    for idx, item in enumerate(l):
      #print "idx: " + str(idx) + ", prev: " + str(prev) + ", item: " + str(item)
      #print "i= ",i
      if item<=prev:
        prev = item
      else:
        #print "at idx: " +str(idx) + " and l[idx] = " + str(l[idx])
        l= [9]*(idx)+ [l[idx]-1] +l[idx+1:]
        prev = l[idx]
      #print l
    
    l.reverse()
    if l[0]==0:
      l=l[1:]
    y = "".join(str(e) for e in l)
    print "Case #%s: %s"%(x,y)