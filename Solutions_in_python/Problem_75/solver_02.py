import sys # For argv

def getCombines(words) : 
 # Get all the combination pairs from a line.
 numCombs = int(words[0])
 combs = []
 for i in range(1,numCombs+1) :
  combs.append((set(words[i][:2]), words[i][2]))
 return combs

def getOppose(words) :
 # Get all the opposition pairs from the latter part of a line.
 numOpps = int(words[0])
 opps = []
 for i in range(1,numOpps+1) :
  opps.append(set(words[i][:2]))
 return opps

def iterate(line, combs, opps) : 
 # Iterate the combination + opposition system. 
 # Check for combinations first:
 for i in combs : 
  # The line length cases stop 'E' from being counted as 'EE'. Hackish.
  if set(line[-2:]) == i[0] and len(line) >= 2:
   line = line[:-2]
   line += i[1]
   return line
 for i in opps :
  if len(i) == 2 :  
   if set(line).issuperset(i) :
    return ""
  else : 
   if line.count(list(i)[0]) == 2 : 
    return ""
 return line

def solve(line,f,caseno) : 
 # Run through a line of the game. Read in the combinations + oppositions, then
 #  the elements themself.
 words = line.split(" ")
 combs = getCombines(words)
 opps = getOppose(words[1+len(combs):])
 elements = words[3+len(combs)+len(opps)]
 line = ""
 # Now, continually add elements and apply necessary changes according to
 #  the combinations and oppositions read in.
 while len(elements) > 0 :
  line += elements[0]
  elements = elements[1:]
  oldLine = None 
  # After adding an element, reduce the line until it is stable.
  while line != oldLine :
   oldLine = line
   line = iterate(line,combs,opps)
 f.write("Case #%d: [%s]\n" % (caseno, ", ".join(map(str,line))))

filename = sys.argv[1]
f = open(filename)
inpt = f.read()
f.close()
inpt_lines = inpt.split("\n")
cases = int(inpt_lines[0])
f = open(sys.argv[2],"w")
caseno = 1
for i in inpt_lines[1:1+cases] :
 solve(i,f,caseno)
 caseno += 1
f.close()

