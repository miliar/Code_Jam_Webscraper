def iround(x):
    return int(round(x) - .5) + (x > 0)

f = open("i1")
t = int(f.readline())
for x in range(1,t+1):
  print "Case #"+str(x)+":",
  n = int(f.readline())
  a = []
  breakable = False
  for i in range(n):
    a.append([""])
    s = f.readline().strip()
    for ss in s:
      if len(a[i][-1]) == 0 or a[i][-1][-1]==ss:
        a[i][-1] += ss
      else:
        a[i].append(ss)
  for i in range(n):
    if len(a[i]) != len(a[0]):
      print "Fegla Won"
      breakable = True
      break
    for j in range(len(a[0])):
      if a[i][j][0] != a[0][j][0]:
        breakable = True        
        print "Fegla Won"
        break
    if breakable: break
  if breakable: continue
  m = 0
  for j in range(len(a[0])):
    z = 0.0
    for i in range(n):
      z += len(a[i][j])
    zz = iround(z/n)
    for i in range(n):
      m += abs(len(a[i][j])-zz)
  print m