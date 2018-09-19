def parseInput(fileName): # Parses the input
  h = open(fileName)
  n = int(h.readline())
  res = [] # Array of parsed input
  for i in range(0, n):
    t = int(h.readline())
    line = h.readline()
    line = line[0:len(line)-1]
    parts = line.split(" ")
    NA = int(parts[0])
    NB = int(parts[1])
    # Parse the timetable from A to B
    AtoB = [];
    for u in range(0, NA):
      line = h.readline()
      line = line[0:len(line)-1]
      parts = line.split(" ")
      AtoB.append([strToMins(parts[0]),strToMins(parts[1])])
    # Parse the timetable from B to A
    BtoA = [];
    for u in range(0, NB):
      line = h.readline()
      line = line[0:len(line)-1]
      parts = line.split(" ")
      BtoA.append([strToMins(parts[0]),strToMins(parts[1])])
    # Add result to the res array
    res.append([t,AtoB,BtoA])
  # Close file and return result
  h.close()
  return res

def strToMins(s):
  parts = s.split(":")
  return int(parts[0])*60 + int(parts[1])

def numTrains(t, A, B): # Finds the number of trains needed to be in A given
                        # the timetables of A and B
  deps = [] # Array of times of departuring trains
  arvs = [] # Array of times of arriving (and ready) trains
  for i in range(0, len(A)):
    deps.append(A[i][0])
  for i in range(0, len(B)):
    arvs.append(B[i][1]+t)
  # Arrange the two arrays
  deps.sort()
  arvs.sort()
  # Check all departing trains one by one ...
  res = 0
  while len(deps) > 0:
    if len(arvs) and arvs[0] <= deps[0]:
      arvs.pop(0)
    else:
      res += 1
    # Remove the departing train just checked
    deps.pop(0)
  # Return the calculated value
  return res

inputs = parseInput("B-large.in") # Parse the input
outputs = ""
for i in range(0, len(inputs)): # Loop over all cases
  outputs += "Case #" + str(i+1) + ": " + str(numTrains(inputs[i][0], inputs[i][1], inputs[i][2])) + " " + str(numTrains(inputs[i][0], inputs[i][2], inputs[i][1])) + "\n"
# Write output to file
h = open("prob-B.out", "w")
h.write(outputs)
h.close()
