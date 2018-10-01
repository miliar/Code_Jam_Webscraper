# code jam 2011 1b a - rpi
# pp@myelin.co.nz

NOISY = 0

T = int(raw_input())

for t in range(T):
    N = int(raw_input())

    teams = []

    matrix = []
    for n in range(N):
        line = raw_input().strip()
        matrix.append(line)

        # work out info for this team
        team = {'id': n}
        wins_against = team['wins_against'] = [idx for idx in range(N) if line[idx] == '1']
        opponents = team['opponents'] = [idx for idx in range(N) if line[idx] != '.']
        team['WP'] = float(len(wins_against)) / len(opponents)
        if NOISY: print team
        teams.append(team)
    if NOISY: print matrix

    # now work out OWP
    for n in range(N):
        team = teams[n]
        owp_cum = 0.0
        for opp_id in team['opponents']:
            opp = teams[opp_id]
            assert n in opp['opponents'], 'opponent mismatch'
            beat_us = 1 if (n in opp['wins_against']) else 0
            temp_wp = float(len(opp['wins_against']) - beat_us) / (len(opp['opponents']) - 1)
            owp_cum += temp_wp
        team['OWP'] = owp_cum / len(team['opponents'])

    # now OOWP
    for n in range(N):
        team = teams[n]
        team['OOWP'] = sum(teams[opp]['OWP'] for opp in team['opponents']) / len(team['opponents'])

    print "Case #%d:" % (t+1)
    for n in range(N):
        team = teams[n]
        if NOISY: print "wp %d owp %d oowp %d" % (team['WP'], team['OWP'], team['OOWP'])
        print 0.25 * team['WP'] + 0.5 * team['OWP'] + 0.25 * team['OOWP']
