def parseInput(fileName): # Parses the input
  h = open(fileName)
  n = int(h.readline())
  res = [] # Array of parsed input
  for i in range(0, n):
    s = int(h.readline())
    se = [] # Array of search engines
    for u in range(0, s):
      line = h.readline()
      se.append(line[0:len(line)-1])
    q = int(h.readline())
    qu = [] # Array of queries
    for u in range(0, q):
      line = h.readline()
      qu.append(line[0:len(line)-1])
    res.append([se,qu])
  # Close file and return result
  h.close()
  return res

def solve(inputs): # Solves for a single case
  se = inputs[0] # Array of search engines
  qu = inputs[1] # Array of queries
  res = 0 # Number of switches
  used = []
  for i in range(0, len(qu)):
    try:
      se.index(qu[i])
      used.append(qu[i])
    except:
      pass
    if len(set(se) - set(used)) == 0:
      used = []
      res += 1
      try:
        se.index(qu[i])
        used.append(qu[i])
      except:
        pass
  # Return the result
  return res

inputs = parseInput("A-large.in") # Parse the input
outputs = ""
for i in range(0, len(inputs)): # Loop over all cases
  outputs += "Case #" + str(i+1) + ": " + str(solve(inputs[i])) + "\n"
# Write output to file
h = open("prob-A.out", "w")
h.write(outputs)
h.close()
