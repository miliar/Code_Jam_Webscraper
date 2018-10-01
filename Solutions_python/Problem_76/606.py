import string
t=int(raw_input(''))

for i in xrange(1,t+1):
  s=0
  n=int(raw_input('')) 
  b=string.split(raw_input(''))
  a=[]
  for j in xrange(len(b)):
   a.append(int(b[j]))
  for j in a:
    s=s^j
  if s!=0:
    print 'Case #'+str(i)+': NO'
    continue

  ma=-1
  for j in range(1,2**n-1):
    bb=bin(j)[2:]
    while len(bb)<n:
      bb='0'+bb
    s1=0
    s2=0
    m1=0
    m2=0
    for d in range(n):
      if bb[d]=='0':
        s1=s1^a[d]
        m1+=a[d]
      else:
        s2=s2^a[d]
        m2+=a[d]
    if s1==s2:
      ma=max(m1,m2,ma)
    
    
  print 'Case #'+str(i)+': '+str(ma)

	
   
