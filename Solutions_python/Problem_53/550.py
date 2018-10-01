import math
import sys

def main(inputFilePath):
  """Main Function for Parsing the input File"""
  cases = []
  try:
    inFile = open(inputFilePath, "r")

    try:
      inputNumber = int(inFile.readline())
      for i in xrange(0,inputNumber):
        cases.append(inFile.readline().split())

      inFile.close()

    finally:
      inFile.close()

  except IOError:
    print "Error reading from file!"

  for i in xrange(0, len(cases)):
    print "Case #%d: %s" % (i+1, LightOnResult(cases[i]))

def LightOnResult(snapperCase):
  """Translates the True/False of the LightOn to the string for output"""
  if LightOn(int(snapperCase[0]), int(snapperCase[1])):
    return "ON"
  return "OFF"

def LightOn(snappers, snaps):
  """ Takes the number of snappers and the number of snaps
      Returns True if the light is on
  """
  snaps = snaps % 2**snappers

  result = (snaps % 2 == 1)
  for i in range(1,snappers):
    snaps /= 2
    result = result and (snaps % 2 == 1)

  return result

if __name__ == "__main__":
  if(len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    print "Supply input file"
