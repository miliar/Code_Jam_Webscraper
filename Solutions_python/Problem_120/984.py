filein = open('A-small-attempt0.in', 'r')
fileout = open('output-small.in', 'w')

def ringNum(A, B):
  r1 = A
  r2 = A+1
  ring = r2**2-r1**2
  total = ring
  count = 0
  while(total <= B):
    count = count+1
    r1 = r1+2
    r2 = r2+2
    ring = r2**2-r1**2
    total = total+ring
  return count


for tc in xrange(1, int(filein.readline())+1):
  A, B = [int(w) for w in filein.readline().split()]
  count = ringNum(A, B)
  res = str('Case #%d: %d' % (tc, count)+'\n')
  fileout.write(res)


fileout.close()
filein.close()
