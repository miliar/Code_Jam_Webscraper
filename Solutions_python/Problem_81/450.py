import math
from collections import defaultdict

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        return cls(input)
    
    def solve(self):
        wins, games = defaultdict(int), defaultdict(int)
        wp, owp, oowp, rpi = {}, {}, {}, {}
        fought = defaultdict(bool)
        teams = self.data
        for i, matches in enumerate(teams):
            for j, result in enumerate(matches):
                if result == '.':
                    continue
                else:
                    games[i] += 1
                    if result == '1':
                        wins[i] += 1
                    fought[(i,j)] = result
        r = range(len(teams))
        for i in r:
            wp[i] = wins[i]/float(games[i])
        for i in r:
            o = []
            for j in r:
                if i == j or not fought[(i,j)]:
                    continue
                res = fought[(i, j)]
                if res == '0':
                    o.append((wins[j]-1)/float(games[j]-1))
                else:
                    o.append(wins[j]/float(games[j]-1))
            owp[i] = sum(o)/float(len(o))
        for i in r:
            o = []
            for j in r:
                if i == j or not fought[(i,j)]:
                    continue
                o.append(owp[j])
            oowp[i] = sum(o)/float(len(o))
        s = []
        for i in r:
            s.append(str(0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]))
        return "\n%s" % "\n".join(s)

f = open("inputs/rpi.txt", "r")
test_cases = int(f.readline())

for i in range(test_cases):
    num_teams = int(f.readline().strip())
    teams = []
    for j in range(num_teams):
        teams.append(f.readline().strip())
    test_case = TestCase.from_input(teams)
    print "Case #%d: %s" % (i+1, test_case.solve())
