import sys

def getMaxScoreIfNotS(v):
  d = v/3
  if (v%3) == 0:
    return d
  else:
    if d <= 9:
      return d+1
    else:
      return 10

def getMaxScoreIfS(v):
  d = v/3
  if (v%3) == 2:
    if d <= 8:
      return d+2
    else:
      return 10
  else:
    if d <= 9:
      return d+1
    else:
      return 10

def computeMaxScoreNotInS():
  rge = range(31)[2:]
  maxNotInS = []
  maxNotInS.append(0)
  maxNotInS.append(0)
  for i in rge:
    maxNotInS.append(getMaxScoreIfNotS(i))
  return maxNotInS

def computeMaxScoreInS():
  rge = range(31)[2:]
  maxInS = []
  maxInS.append(0)
  maxInS.append(0)
  for i in rge:
    maxInS.append(getMaxScoreIfS(i))
  return maxInS

def solvePb(n, s, p, vals, maxInS, maxNotInS):
  nbNaturallyOver = 0
  nbNeedingToBeOver = 0
  for val in vals:
    val = int(val)
    if maxNotInS[val] >= p:
      nbNaturallyOver += 1
    elif maxInS[val] >= p:
      nbNeedingToBeOver += 1
  return nbNaturallyOver + min(s,nbNeedingToBeOver)

def solve(pathI,pathOut):
  maxN = computeMaxScoreNotInS()
  maxI = computeMaxScoreInS()
  counter = 1
  fI = file(pathI,'rU')
  fO = file(pathOut,'w')
  lines = fI.readlines()
  for line in lines[1:]:
    elem = line.split()
    n = int(elem[0])
    s = int(elem[1])
    p = int(elem[2])
    vals = elem[3:]
    sol = solvePb(n,s,p,vals,maxI,maxN)
    fO.write('Case #')
    fO.write(str(counter))
    fO.write(': ')
    fO.write(str(sol))
    fO.write('\n')
    counter+=1
  fI.close()
  fO.close()



def main():
  args = sys.argv[1:]
  solve(args[0],args[1])


main()
