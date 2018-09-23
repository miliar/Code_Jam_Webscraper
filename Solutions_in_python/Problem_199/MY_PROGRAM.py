t = int(raw_input())  # read a line with a single integer

def changesign(s):
  if s == "-":
    return "+"
  else:
    return "-"

for i in xrange(1, t + 1):
  ss, n = raw_input().split()
  s = list(ss)
  tries = 0
  numtoflip = int(n)
  impossible = False
  while len(s) != 0:
    while len(s) != 0 and s[0] is "+":
      del s[0]
    if len(s) != 0 and s[0] is "-":
      if len(s) < numtoflip:
        print "Case #"+str(i)+": IMPOSSIBLE"
        impossible = True
        break
      else:
        for j in xrange(numtoflip):
          s[j] = changesign(s[j])
        tries += 1
        del s[0]
  if impossible is False:
    print "Case #"+str(i)+": " + str(tries)
  
    
  

