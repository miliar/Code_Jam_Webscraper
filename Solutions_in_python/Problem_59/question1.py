

#f = open('test_q1.txt')
#f = open('Downloads/A-small-attempt0.in')
f = open('Downloads/A-large.in')

case = int(f.readline().strip())
for i in xrange(1,case+1):
#for i in xrange(1,3):
  n, m = map(int,f.readline().strip().split())
  exist_path = []
  expect_path = []
  for j in xrange(n):
    x = f.readline().strip()[1:].split('/')
    for k in xrange(len(x)):
      p = ''.join(x[:k+1])
      #print p
      if k >= len(exist_path):
        exist_path.append([ p ])
      elif p not in exist_path[k]:
        exist_path[k].append(p)
  #print 'ex',exist_path
    
  result = 0
  for j in xrange(m):
    x = f.readline().strip()[1:].split('/')
    for k in range(len(x)):
      p = ''.join(x[:k+1])
      #print 'p',p
      if k >= len(exist_path):
        result += 1
        exist_path.append([p])
      elif p not in exist_path[k]:
        result += 1
        exist_path[k].append(p)
  #print 'ex',exist_path

  print 'Case #%d:'%i,result
