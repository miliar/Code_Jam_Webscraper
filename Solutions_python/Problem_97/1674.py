f = open('small.in')

T = int(f.readline())

for t in range(1,T+1):
  recycled = 0
  line = f.readline().split(' ')
  A,B = int(line[0]), int(line[1])
  for m in range(A,B+1):
    m_str = str(m)
    for n in range(A, m):
      n_str = str(n)
      for i in range(0,len(n_str)):
        nn_str = n_str[i:] + n_str[:i]
        if nn_str == m_str:
          recycled += 1 
          break
        
  print "Case #%i: %i"%(t,recycled)
