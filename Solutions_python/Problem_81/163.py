def main():
  fh = open("A-large.in", 'r')
  T = int(fh.readline())
  case = 1
  
  while T > 0:
    getInfo(fh, case)
    T = T - 1
    case = case + 1

def getInfo(fh, case):
  numTeams = int(fh.readline())
  records = []
  RPI = []
  WP = []
  OWP = []
  OOWP = []

  for i in range(numTeams):
    records.append(fh.readline().strip())
    wins = 0
    losses = 0
    for j in range(len(records[i])):
      if records[i][j] == "0":
        losses += 1
      elif records[i][j] == "1":
        wins += 1
    WP.append([float(wins)/(wins+losses), losses, wins])

  for k in range(numTeams):
    numOpp = 0
    answer = 0
    for l in range(len(records[k])):
      if records[k][l] == "0":
        numOpp += 1
        answer += ((float(WP[l][2])-1)/float(float(WP[l][1])+float(WP[l][2]-1)))
      elif records[k][l] == "1":
        numOpp += 1
        answer += ((float(WP[l][2]))/float(float(WP[l][2])+float(WP[l][1]-1)))
    OWP.append(float(1/float(numOpp))*float(answer))

  for m in range(numTeams):
    numOpp = 0
    answer = 0
    for n in range(len(records[m])):
      if not(records[m][n] == "."):
        numOpp += 1
        answer += float(OWP[n])
    OOWP.append(float(1/float(numOpp)) * float(answer))

  print "Case #" + str(case) + ":"

  for o in range(numTeams):
    print str((.25*WP[o][0]) + (.5 * OWP[o]) + (.25*OOWP[o]))
      




main()
