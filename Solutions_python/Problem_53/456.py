fileName = "A-large"

inputFile = open( fileName + ".in", "r" )
outputFile = open( fileName + ".out", "w" )

numCases = int(inputFile.readline())

for caseNumber in range(1, numCases + 1):

  input_s = inputFile.readline()
  
  numSnappers = int(input_s.split()[0])
  numSnaps    = int(input_s.split()[1])
  
  mask = (2**numSnappers) - 1
  
  if mask == numSnaps & mask:
    answer = "ON"
  else:
    answer = "OFF"

  # Output the results
  outputFile.write( "Case #%d: %s\n" % (caseNumber, answer) )

# Close the streams
inputFile.close()
outputFile.close()
