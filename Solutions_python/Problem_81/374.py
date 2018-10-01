import sys
import getopt
import itertools

def solve_case(num, teams, lines, line_num):
    games = []
    team_info = []
    answer = ''

    for i in range(1, teams + 1):
        line = lines[line_num + i]

        games.append([]);
        for score in line:
            if score != '\n':
                games[i-1].append(score)

    for team in games:
        num_played = 0
        num_won = 0

        for game in team:
            if game != '.':
                num_played += 1
            else:
                continue

            if game == '1':
                num_won += 1

        WP = float(num_won) / num_played 
        team_info.append({
            'WP': WP,
            'OWP': 0,
            'OOWP': 0,
        })

    for i in range(0, len(team_info)):
        team = team_info[i]
        owp = []

        opps = []
        for g in games[i]:
            if g != '.':
                opps.append(True)
            else:
                opps.append(False)

        for j in range(0, len(team_info)):
            if i == j or not opps[j]:
                continue

            num_played = 0
            num_won = 0
            for k in range(0, len(games[j])):
                if k == i:
                    continue

                game = games[j][k]
                if game != '.':
                    num_played += 1
                else:
                    continue

                if game == '1':
                    num_won += 1

            if num_played == 0:
                owp.append(0)
            else:
                owp.append(float(num_won) / num_played)

        owps = 0
        for wp in owp:
            owps += wp

        team['OWP'] = float(owps) / len(owp)

    for i in range(0, len(team_info)):
        team = team_info[i]
        oowp = []

        opps = []
        for g in games[i]:
            if g != '.':
                opps.append(True)
            else:
                opps.append(False)

        for j in range(0, len(team_info)):
            if (i == j) or not opps[j]:
                continue

            oowp.append(team_info[j]['OWP'])

        oowps = 0
        for owp in oowp:
            oowps += owp

        team['OOWP'] = float(oowps) / len(oowp)

    answer += 'Case #%d:\n' % num

    for team in team_info:
        RPI = (0.25 * team['WP']) + (0.5 * team['OWP']) + (0.25 * team['OOWP'])
        answer += '%s\n' % RPI

    return answer

def solve(argv):
    file = argv[1]
    with open(file, 'r') as f:
        lines = f.readlines()

    with open('a.out', 'w') as f:
        N = int(lines[0])
        
        line_num = 1
        for i in range(1, N + 1):
            teams = int(lines[line_num])
            out = solve_case(i, teams, lines, line_num)
            f.write(out)
            line_num += (teams + 1)

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'h', ['help'])
        except getopt.error, msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, 'for help use --help'
        return 2

    solve(argv)

if __name__ == '__main__':
    sys.exit(main())
