N=int(raw_input())

for i in xrange(1,N+1):
  [a,b]=raw_input().split()
  n = len(a)
  res=0
  for k in xrange(int(a),int(b)+1):
    s = {}
    for p in xrange(1,n):
      num = (k/(10**(n-p)) + (10**p)*k) % (10**n)
      if num in s:
        continue
      s[num] = True
      if num > k and num <= int(b):
        res += 1
  print "Case #%d: %d" % (i,res)
      


