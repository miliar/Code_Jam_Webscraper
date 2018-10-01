f = open('A-large.in','r')
out = open('largeoutput.txt','w')

numcases = int(f.readline())

for casenum in range(numcases):
    
    numTeams = int(f.readline())
    allTeams = []
    
    numWins = []
    totalGames = []
    
    for team in range(numTeams):
        line = f.readline().strip()
        
        allTeams.append([])
        numWins.append(0)
        totalGames.append(0)
        
        for result in line:
            allTeams[team].append(result)
            if(result != '.'):
                totalGames[team] += 1
                if(result == '1'):
                    numWins[team] += 1
        
    out.write('Case #%d:\n' % (casenum+1))
    
    all_wp = []
    all_owp = []
    all_oowp = []
    
    for team in range(numTeams):
        
        # calculate this team's WP
        all_wp.append(float(numWins[team]) / float(totalGames[team]))
        #print (team+1), ' wp = ', all_wp[team]
        
        total_other_wp = 0
        total_opponents = 0
        
        for opponent in range(numTeams):
            # you never played yourself
            if(opponent == team):
                continue
            if(allTeams[team][opponent] == '.'):
                continue
            
            total_opponents += 1
            oppWins = 0
            oppTotal = 0
            
            for game in range(numTeams):
                # ignore games they played against you
                if(game == team):
                    continue
                    
                outcome = allTeams[opponent][game]
                if(outcome != '.'):
                    oppTotal += 1
                    if(outcome == '1'):
                        oppWins += 1
    
            total_other_wp += float(oppWins) / float(oppTotal)
        
        all_owp.append(float(total_other_wp) / float(total_opponents))
        #print (team+1), ' owp = ', all_owp[team]
    
    for team in range(numTeams):
        
        total_owp = 0
        total_opponents = 0
        
        for opponent in range(numTeams):
            if(opponent == team):
                continue
            if(allTeams[team][opponent] == '.'):
                continue
            total_opponents += 1
            total_owp += all_owp[opponent]
        
        all_oowp.append(float(total_owp) / float(total_opponents))
        #print (team+1), ' oowp = ', all_oowp[team]
    
    for team in range(numTeams):
        rpi = 0.25 * all_wp[team] + 0.5 * all_owp[team] + 0.25 * all_oowp[team]
        out.write('%f\n' % rpi)

out.close()