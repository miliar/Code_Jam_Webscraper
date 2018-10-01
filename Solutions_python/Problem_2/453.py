from copy import deepcopy

def addMinutes(ls, turn):
  print ls
  ls[1] = ls[1] + turn
  if ls[1] >= 60 :
    ls[0] = ls[0] + 1
    ls[1] = ls[1] - 60
  return ls

f = open("B-small-attempt0.in","r")
out = open("B-small.out","w")
cases = int(f.readline())
for c in range(1,cases+1):
  turn = int(f.readline())
  ns = [int(n) for n in f.readline().strip('\n').split()]
  na = ns[0]
  nb = ns[1]
  tripsA = []
  tripsAused = []
  tripsB = []
  tripsBused = []
  for a in range(na):
    auxA = [s.split(":") for s in f.readline().strip('\n').split()]
    trip = []
    trip.append(int(auxA[0][0]))
    trip.append(int(auxA[0][1]))
    trip.append(int(auxA[1][0]))
    trip.append(int(auxA[1][1]))
    tripsA.append(deepcopy(trip))
    tripsAused.append(True)
  for b in range(nb):
    auxB = [s.split(":") for s in f.readline().strip('\n').split()]
    trip = []
    trip.append(int(auxB[0][0]))
    trip.append(int(auxB[0][1]))
    trip.append(int(auxB[1][0]))
    trip.append(int(auxB[1][1]))
    tripsB.append(deepcopy(trip))
    tripsBused.append(True)

  tripsA.sort()
  tripsB.sort()
  
  for t in tripsA:
    for tb in tripsB:
      if (tripsBused[tripsB.index(tb)] == True) :
        arrivalAtAFromB = tb[2:]
        depFromA = t[:2]
        updatedTime = addMinutes(arrivalAtAFromB,turn)
        if(depFromA >= updatedTime):
          tripsBused[tripsB.index(tb)] = False
          na = na -1
          break
  for t in tripsB:
    for ta in tripsA:
      if (tripsAused[tripsA.index(ta)] == True) :
        arrivalAtBFromA = ta[2:]
        depFromB = t[:2]
        updatedTime = addMinutes(arrivalAtBFromA,turn)
        if(depFromB >= updatedTime):
          tripsAused[tripsA.index(ta)] = False
          nb = nb -1
          break
  out.write("Case #%d: %d %d\n" %(c,na,nb))
  
f.close()
out.close()