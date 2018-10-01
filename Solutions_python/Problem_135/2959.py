import sys

def readAnswer(infile):
  answer1 = int(infile.readline())
  answer_row = None
  for line in range(4):
    curr_line = infile.readline()
    if line == answer1 - 1:
      result = [int(v) for v in curr_line.split()]
  return set(result)

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  answer1 = readAnswer(infile)
  answer2 = readAnswer(infile)
  
  intersection = answer1 & answer2
  
  if len(intersection) == 0:
    print "Volunteer cheated!"
  elif len(intersection) == 1:
    print intersection.pop()
  else:
    print "Bad magician!"
  
infile.close()