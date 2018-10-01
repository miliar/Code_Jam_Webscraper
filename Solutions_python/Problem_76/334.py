#!/usr/bin/python

ri = raw_input

for t in xrange(int(ri())):
  ri()
  vals = map(int,ri().split())
  if reduce(lambda x,y:x^y,vals,0)==0:
    print "Case #%d: %d" % (t+1,sum(vals)-min(vals))
  else:
    print "Case #%d: NO" % (t+1)

