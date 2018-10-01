import sys
 
def solve(thestr):
   a = thestr.split(' ')
   p = [c for c in a[0]]
   size = int(a[1])
   toflip = ''.join(a[0].split('+'))
      
   pos = 0
   changes = 0
   while pos <= (len(p) - size):
      if p[pos] == '-':
         changes += 1
         for x in range(size):
             p[pos+x] = '+' if p[pos+x] == '-' else '-'
      pos += 1

   finalp = ''.join(p)
   expected = '+'*len(p)

   return str(changes) if finalp == expected else "IMPOSSIBLE"

 
 
for tc in xrange(1, int(sys.stdin.readline())+1):
    msg = sys.stdin.readline().strip()
 
    best = solve(msg)
    print 'Case #%d: %s' % (tc, best)
