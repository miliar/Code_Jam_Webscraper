#!/usr/bin/python3

class Team():
  def __init__(self, team_num):
    self.wins = []
    self.losses = []
    self.team_num = team_num

  def process_line(self, line):
    for team, game in enumerate(line):
      if game == '1':
        self.wins.append(team)
      if game == '0':
        self.losses.append(team)

  def WP(self,):
    wins = len(self.wins)
    games_played = len(self.wins) + len(self.losses)
    return wins/games_played

  def WP_without_team(self, team):
    wins = len(self.wins)
    games_played = len(self.wins) + len(self.losses)
    if team in self.wins:
      wins -= 1
      games_played -= 1
    elif team in self.losses:
      games_played -= 1
    else:
      print("error!")
    return wins/games_played

  def OWP(self, teams):
    opponents = self.wins + self.losses
    sum = 0
    for opponent in opponents:
      op_WP = teams[opponent].WP_without_team(self.team_num)
      # print("team" + str(opponent) + " wp against " + str(self.team_num)
      #       + ": " + str(op_WP))
      sum += op_WP
    return sum/len(opponents)

  def OOWP(self, teams):
    opponents = self.wins + self.losses
    sum = 0
    for opponent in opponents:
      op_OWP = teams[opponent].OWP(teams)
      sum += op_OWP
    return sum/len(opponents)

  def RPI(self, teams):
    rpi = .25 * self.WP() + .50 * self.OWP(teams) + .25 * self.OOWP(teams)
    return rpi

def main(problem = ''):
  with open('{0}.out'.format(problem), 'w') as out_file:
    with open('{0}.in'.format(problem), 'r') as in_file:
      num_cases = int(in_file.readline())
      for case_num in range(1, num_cases + 1):
        num_teams = int(in_file.readline())
        teams = []
        for team_num in range(0, num_teams):
          team = Team(team_num)
          team.process_line(in_file.readline())
          teams.append(team)

        out_file.write('Case #{0}:\n'.format(case_num))
        for team in teams:
          out_file.write('{0}\n'.format(team.RPI(teams)))

main('A-large')
