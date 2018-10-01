import sys
import decimal

def dbg(s):
  sys.stderr.write( "%s\n" % s )
  #pass

i = open( "A-large.in" )

n = i.readline().strip()

for idx in xrange(1, int(n)+1):
  input = i.readline().strip()
  #list = input.split('')
  m = dict()
  current = 1
  for l in input:
    #dbg( "testing: %c" % l )
    if not m.has_key( l ):
      m[l] = current
      if current == 1:
        current = 0
      elif current == 0:
        current = 2
      else:
        current += 1
  # now translate
  base = current
  #dbg( "base is %i" % base )
  if base < 2:
    base = 2
  total = decimal.Decimal(0)
  exponent = decimal.Decimal(1)
  for l in input[::-1]:
    interm = decimal.getcontext().multiply( decimal.Decimal(m[l]), exponent )
    total = decimal.getcontext().add( total, interm )
    exponent = decimal.getcontext().multiply( exponent, base )
    #dbg( "after %s total is %i exp %i" % ( l, total, exponent ) )

  #dbg( "Case #%i: %i" % (idx, total) )
  print "Case #%i: %s" % (idx, total)
