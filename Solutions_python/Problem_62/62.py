import math
import sys

def main(inputFilePath):
  cases = []
  try:
    inFile = open(inputFilePath, "r")

    try:
      caseCount = int(inFile.readline())
      for i in xrange(0,caseCount):
        wireCount = int(inFile.readline())
        case = []
        for j in xrange(0,wireCount):
          wire = inFile.readline().split()
          map(int, wire)
          case.append(wire)
        cases.append(case)

      inFile.close()

    finally:
      inFile.close()

  except IOError:
    print "Error reading from file!"

  for i in xrange(0, len(cases)):
    print "Case #%d: %s" % (i+1, caseResult(cases[i]))

def caseResult(case):
  count = 0
  for i in xrange(0, len(case)):
    start = int(case[i][0])
    end = int(case[i][1])
    for j in xrange(i, len(case)):
      if (int(case[j][0]) > start and int(case[j][1]) < end) or (int(case[j][0]) < start and int(case[j][1]) > end):
        count += 1

  return count



if __name__ == "__main__":
  if(len(sys.argv) > 1):
    main(sys.argv[1])
  else:
    print "Supply input file"


