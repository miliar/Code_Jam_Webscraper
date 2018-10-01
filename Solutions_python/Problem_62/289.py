for case in xrange(input()):
   n = int(raw_input())
   wires = sorted([[int(c) for c in raw_input().split()] for i in xrange(n)])
   ai, bi = zip(*wires)
   count = 0
   for i, h in enumerate(bi):
      count += len([x for x in bi[i+1:] if x<h])
   print 'Case #%d: %d' % (case+1, count)
