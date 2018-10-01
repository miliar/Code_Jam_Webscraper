for case in xrange(input()):
   n, k = [int(s) for s in raw_input().split()]
   k2 = str(bin(k))[-n:]
   ones = [1 for d in k2 if d == '1']
   l = len(ones) == len(k2) and 'ON' or 'OFF'
   print 'Case #%d: %s' % (case+1, l)
