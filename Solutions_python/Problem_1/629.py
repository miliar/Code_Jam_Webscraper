def function(nbEngines) :
  engines = {}
  for i in range(nbEngines) :
    engine = f.readline().strip()
    engines[engine] = [0, -1, engine, 0]
  nbQueries = int(f.readline())
  lastQuery = ''
  queries = []
  engineList = engines.keys()
  # we must count forced transitions, a forced transition occurs whenever you've found a query of every search engine including the one you are using
  result = 0
  for i in range(nbQueries) :
    query = f.readline().strip()
    if query in engines :
      if query in engineList :
        engineList.remove(query)
      if engineList == [] :
        result += 1
        engineList = engines.keys()
        engineList.remove(query)
  return result  

fn = "test"
fn = "A-small-attempt0"
#fn = "A-large"
open(fn + '.out', 'w')

def caseOut(case, fn, line) :
  open(fn + ".out", "a").write("Case #%s: %s\n" % (case, line))

f = open(fn + ".in")
try :
  cases = int(f.readline()) 
  for case in range(cases + 1)[1:] :
    caseOut(case, fn, function(int(f.readline())))
finally :
  f.close()  