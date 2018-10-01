import sys, re

class Player():

  def __init__(self):
    self.won = 0
    self.played = 0
    self.OWP = 0.0
    self.OOWP = 0.0
    self.games = []

  def WP(self):
    return self.won/float(self.played)

  def WPwithout(self, ind):
    if self.games[ind]=='.': return self.WP()
    if self.games[ind]=='0': 
      if self.played-1==0: return 0
      return self.won/float(self.played-1)
    if self.games[ind]=='1': 
      if self.played-1==0: return 0
      return (self.won-1)/float(self.played-1)

  def RPI(self):
    return 0.25 * self.WP() + 0.50 * self.OWP + 0.25 * self.OOWP



cases = sys.stdin.readline()

for case in range(0,int(cases)):
  N = int(sys.stdin.readline())
  games = []
  for i in range(0,int(N)):
    games.append(sys.stdin.readline())
  players = [Player() for x in range(0,N)]

  i = 0
  for game in games:
    players[i].games = game
    for p in game:
      if p=='1':
        players[i].won+=1
        players[i].played+=1
      if p=='0':
        players[i].played+=1
    i+=1

  for j in range(0,N):
    owpCount=0
    for k in range(0,N):
      if k==j: continue
      if players[j].games[k]=='.': continue
      players[j].OWP += players[k].WPwithout(j)
      owpCount+=1
    players[j].OWP/=float(owpCount)

  for j in range(0,N):
    owpCount=0
    for k in range(0,N):
      if k==j: continue
      if players[j].games[k]=='.': continue
      players[j].OOWP += players[k].OWP
      owpCount+=1
    players[j].OOWP/=float(owpCount)
  

  print "Case #%d:" % (case+1)
  for i in range(0,N):
    print players[i].RPI()

