f = open("A-large.in","r")
out = open("A-large.out","w")
cases = int(f.readline())
for c in range(1,cases+1):
  switches = 0
  engines = []
  nSE = int(f.readline())
  for s in range(nSE):
    eng = f.readline().strip('\n')
    engines.append(eng)
  nQ = int(f.readline())
  true = set(engines)
  for q in range(nQ):
    qs = f.readline().strip('\n')
    if true.__contains__(qs):
      true.remove(qs)
    if (true.__len__() == 0):
      switches = switches + 1
      true = set(engines)
      true.remove(qs)
  out.write("Case #%d: %d\n" %(c,switches))
f.close()
out.close()