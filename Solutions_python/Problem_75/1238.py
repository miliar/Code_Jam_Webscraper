
f = open( "1", "r" )
l = f.readlines()

tests = int(l[0])

for i in xrange(1, tests+1):
  #print "test", i
  # cs c c ds d d ns nnnn
  line = l[i].split( ' ' )
  # base count
  cs = int(line[0])
  #print "cs", cs
  bases = {}
  for c in xrange(0, cs):
    base = line[c+1]
    #print "base", base
    bases[ base[0] + base[1] ] = base[2]
    bases[ base[1] + base[0] ] = base[2]

  #print bases

  # opposed count
  ds = int( line[cs+1] )
  #print "ds", ds
  opposed = {}
  for d in xrange(0, ds):
    oppose = line[cs+2+d] # 2 characters
    opposed[ oppose[0] ] = oppose[1]
    opposed[ oppose[1] ] = oppose[0]

  #print opposed

  ns = int( line[cs+ds+2] )
  #print "ns", ns
  
  result = []
  for n in xrange(0,ns):
    element = line[cs+ds+3][n]
    result.append( element )
    
    if len(result) > 1:
      base = result[-1] + result[-2]
      if bases.has_key( base ):
        result.pop()
        result.pop()
        result.append( bases[base] )

      if opposed.has_key( result[-1] ) and opposed[result[-1]] in result[0:-1]:
        result = []

  print "Case #%i: [%s]" % ( i, ", ".join( result ) )
