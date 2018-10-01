for case in xrange(int(raw_input())):
    print 'Case #%d:' % (case+1)
    games = []
    numTeams = int(raw_input())
    for i in xrange(numTeams):
        games.append(raw_input())

    #rpi = 0.25 * wp + 0.5 * owp + 0.25 * oowp
    teams = [None] * numTeams
    WP = [None] * numTeams
    for i in xrange(numTeams):
        ngames = 0
        wins = 0
        for j in range(numTeams):
            if games[i][j] in '01':
                ngames += 1
            if games[i][j] == '1':
                wins += 1
        WP[i] = float(wins)/ngames
        teams[i] = (wins, ngames)

    #Calculate OWP
    OWP = [None] * numTeams
    for i in xrange(numTeams):
        wp = 0
        #WP for each
        for j in xrange(numTeams):
            #i won j
            if games[i][j] == '1':
                wp += float(teams[j][0]) / (teams[j][1] -1)
            #i lost to j
            elif games[i][j] == '0':
                wp += float(teams[j][0]-1) / (teams[j][1] -1)

        wp = float(wp) /teams[i][1]
        OWP[i] = wp

    for i in xrange(numTeams):
        a=0
        b=0
        for j in xrange(numTeams):
            if i == j:
                continue
            if games[i][j] == '.':
                continue
            b+=1
            a+= OWP[j]
        a = float(a) / b

        RPI = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * a
        print RPI
