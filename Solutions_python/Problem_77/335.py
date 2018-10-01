infile = open('D-small-attempt0.in')
num_cases = readint()
for iter in range(1,num_cases+1):
  n = readint()
  x = [int(float(x))-1 for x in infile.readline().split()]
  c = 0.0
  for i in range(len(x)):
    if x[i] != i:
      c = c + 1
  print "Case #" + str(iter) + ": " + str(c)