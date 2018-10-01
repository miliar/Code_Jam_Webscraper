filename = 'large'

rpi = lambda wp, owp, oowp: 0.25 * wp + 0.50 * owp + 0.25 * oowp

def solve(qtd_teams, lines):
    teams = {}
    for i in xrange(qtd_teams):
        line = lines[i]
        plays = [None if x == '.' else x == '1' for x in line]
        won = plays.count(True)
        lost = plays.count(False)
        played = won + lost
        teams[i] = {
            'plays': plays,
            'won': won,
            'lost': lost,
            'played': played,
            'wp': float(won) / played
        }
    for i in xrange(qtd_teams):
        team = teams[i]
        owps = []
        for j in xrange(qtd_teams):
            if j == i:
                continue
            opponent = teams[j]
            if opponent['plays'][i] == None:
                continue
            games = [x for x in opponent['plays']]
            games.pop(i)
            won = games.count(True)
            lost = games.count(False)
            played = won + lost
            owps.append(float(won) / played)
        teams[i]['owp'] = sum(owps) / len(owps)
    for i in xrange(qtd_teams):
        team = teams[i]
        oowps = []
        for j in xrange(qtd_teams):
            if j == i:
                continue
            opponent = teams[j]
            if opponent['plays'][i] == None:
                continue
            oowps.append(opponent['owp'])
        teams[i]['oowp'] = sum(oowps) / len(oowps)
        teams[i]['rpi'] = rpi(teams[i]['wp'], teams[i]['owp'], teams[i]['oowp'])
    results = [''] + [str(teams[x]['rpi']) for x in xrange(qtd_teams)]
    return '\n'.join(results)

def main():
    file_in = open('A-%s.in' % filename)
    file_out = open('A-%s.out' % filename, 'w')
    cases = int(file_in.readline().strip())
    for case in xrange(1, cases + 1):
        teams = int(file_in.readline().strip())
        lines = []
        for i in xrange(teams):
            lines.append(file_in.readline().strip())
        result = solve(teams, lines)
        file_out.write('Case #%d: %s\n' % (case, result))
    file_out.close()
    file_in.close()
    return

if __name__ == '__main__':
    main()
    import sys
    sys.exit(0)
