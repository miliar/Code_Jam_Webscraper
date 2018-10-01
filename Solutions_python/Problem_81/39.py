from sys import stdin

testcases = int(stdin.readline())

for case in xrange(testcases):

    num_teams = int(stdin.readline())

    matches = []
    results = []
    wp = []
    owp = []
    oowp = []
    opponents = []

    for _ in xrange(num_teams):
        team_matches = stdin.readline().strip()
        team_opponents = []
        wins = 0
        losses = 0
        for i in xrange(num_teams):
            if team_matches[i] == "1":
                team_opponents.append(i)
                wins += 1
            elif team_matches[i] == "0":
                team_opponents.append(i)
                losses += 1
        results.append((wins, losses))
        wp.append(float(wins) / (wins + losses))
                   
        opponents.append(team_opponents)
        matches.append(team_matches)
    
    for j in xrange(num_teams):
        owp_total = 0
        for opp in opponents[j]:
            wins, losses = results[opp]
            if matches[opp][j] == "1":
                wins -= 1
            else:
                losses -= 1
            owp_total += float(wins) / (wins + losses)
        owp.append(owp_total / len(opponents[j]))

    for k in xrange(num_teams):
        oowp_total = 0
        for opp in opponents[k]:
            oowp_total += owp[opp]
        oowp.append(oowp_total / len(opponents[k]))
    
    print("Case #%d:" % (case+1))
    for l in xrange(num_teams):
        rpi = 0.25 * (wp[l] + owp[l] + owp[l] + oowp[l])
        print("%.12f" % rpi)
