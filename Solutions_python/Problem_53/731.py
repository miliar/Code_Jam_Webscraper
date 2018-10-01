print 'snap'
f = "mytest"
#f = 'A-large-attempt0'
#f = sys.stdin
infile = open("A-large.in", "r")
outfile = open("op-click2.out", "w")

def ReadInts():
  return list(map(int, infile.readline().strip().split(" ")))

T = ReadInts()[0]
for each in range (1, T+1):
  (N, K) = ReadInts()
  os = (K+1)%(2**N)
  if os == 0:
    op = 'ON'
  else : op = 'OFF'
  print "Case #%d: %s" % (each, op)
  outfile.write("Case #%d: %s\n" % (each, op))
  
