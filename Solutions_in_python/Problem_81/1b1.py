#!/usr/bin/python
import sys
import string

# Open in- and output files
f = "" if len(sys.argv) < 2 else sys.argv[1]
i = open(f, 'r')
o = open("%s.out" % f, 'w')

# Parse input file
cases = int(i.readline())

for case in range(1, cases + 1):  
  # chunks = i.readline().strip().split(" ")
  # OR
  # value = int(i.readline())
  teams = int(i.readline())

  # Step 1: Build 2 dim array
  stats = []
  rpival = []

  for n in range(0,teams):
    statsline = i.readline().strip()
    stats.append([])
    rpival.append(dict(wp=0, owp=0, oowp=0, games=0))
    for c in range(0,len(statsline)):
        stats[n].append(statsline[c])
    
  # calc wp
  for team in range(0, teams):
    print "Calcing Team " + str(team)
    wins = 0
    losses = 0
    for game in stats[team]:
      print game
      if game == '1':
        wins += 1
      if game == '0':
        losses += 1
    print "WL" + str(wins) + " " + str(losses)
    rpival[team]['wp'] = float(wins) / (wins+losses)
    rpival[team]['games'] = wins + losses

  # calc owp
  for team in range(0,teams):
    print "OWP " + str(team)
    owp = 0
    for op in range(0,teams):
      if op != team and stats[team][op] != '.':
        if stats[op][team] == '1':
          owp += (((rpival[op]['wp'] * rpival[op]['games']) - 1) / (rpival[op]['games'] - 1))
        else:
          owp += ((rpival[op]['wp'] * rpival[op]['games']) / (rpival[op]['games'] - 1))
    rpival[team]['owp'] = float(owp) / (rpival[team]['games'])

  # calc oowp
  for team in range(0,teams):
    print "OOWP " + str(team)
    oowp = 0
    for op in range(0, teams):
        if op != team and stats[team][op] != '.':
          oowp += rpival[op]['owp']
    rpival[team]['oowp'] = float(oowp) / (rpival[team]['games'])

  print stats
  print rpival
 
  # calc RPI
  output = ""
  for team in range(0,teams):
    rpi = 0.25 * rpival[team]['wp'] + 0.5 * rpival[team]['owp'] + 0.25 * rpival[team]['oowp']
    output += "%f\n" % rpi

  result = "Case #%i:\n%s" % (case, output)
  print result
  o.write("%s\n" % result)

# Close in- and output
i.close()
o.close()
