def findNext( queries, engines ):
  enginescopy = list( engines )
  for engine in enginescopy: #fastcheck
    if not engine in queries:
      return None
  for query in queries:
    if query in enginescopy:
      if len( enginescopy ) == 1:
        return queries [ queries.index( enginescopy[0] ) : ]
      else:
        enginescopy.pop( enginescopy.index(query) )
  try:
    return queries [ queries.index( enginescopy[0] ) : ]
  except ValueError:
    return None


f   = open('SavingTheUniverse.in')
out = open('SavingTheUniverse.out' , 'w')

lines = f.readlines()
ncases = int( lines[0].rstrip('\n') )
next = 1

for i in range( ncases ):
  engines  = []
  queries  = []

  nengines = int ( lines[next].rstrip('\n') )
  next += 1
  for j in range( nengines ):
    engines.append( lines[ next+j ].rstrip('\n') )
  next += nengines
  nqueries = int( lines[next].rstrip('\n') )
  next += 1
  for j in range( nqueries ):
    queries.append( lines[ next+j ].rstrip('\n') )
  next += nqueries
  # print "---------------------"
  # print "Case #%s" %(i+1)
  # print "Engines:"  
  # for engine in engines:
  #   print "  %s" %(engine)
  # print "Queries:"
  # for query in queries:
  #   print "  %s" %(query)

  actualengine = None
  nswitches = 0
  # while True:
  while True:
    queries = findNext( queries, engines )
    if not queries:
      print "Case #%s: %s" %( i+1 , nswitches )
      out.write( "Case #%s: %s\n" %( i+1 , nswitches ) )
      break
    nswitches += 1