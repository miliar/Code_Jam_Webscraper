import sys, fractions

if (len(sys.argv) < 2):
  print("No file specified")
  sys.exit(1)
  
infile = open(sys.argv[1])
outfile = open(sys.argv[1] + ".out", "w")

num_cases = int(infile.readline().strip())

for case in range(1, num_cases+1):

  line_parts = map(int,map(str.strip, infile.readline().split()))

  n = line_parts[0]
  great_events = line_parts[1:]
  
  great_events.sort()
  
  factor = 0
  
  for i in range(len(great_events) - 1):
    factor = fractions.gcd(factor, great_events[i+1] - great_events[i])
    
  if great_events[0] % factor == 0:
    result = 0
  else:
    iters = (great_events[0] / factor) + 1
    result = factor * iters - great_events[0]
   
  outfile.write("Case #%d: %d\n" % (case, result))
  
  if case % 100 == 0:
    print("Completed case %d" % case)
    
outfile.close()
infile.close()
  
    