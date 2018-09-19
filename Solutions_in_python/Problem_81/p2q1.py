'''
Created on 2011-05-20

@author: jason
'''

def main():
    
    fi = open("A-large.in","r")
    fo = open("output", "w")
    
    lines = []
    for line in fi:
        lines.append(line)
    
    lines = lines[1:]
    
    linecount = 0
    tourns = []
    while linecount < len(lines):
        teams = []
        intgames = int(lines[linecount])
        for team in range(linecount+1,linecount+intgames+1):
            teamline = lines[team]
            teamstats = []
            if teamline[-1] == '\n':
                teamline = teamline[:-1]
            for stat in teamline:
                teamstats.append(stat)
            teams.append(teamstats)
        tourns.append(teams)
        linecount = linecount + intgames + 1
        
    print tourns
    
    for count, tourn in enumerate(tourns):
        results = []
        for index, team in enumerate(tourn):
            teamresults = []
            #calc score
            gamesplayed = 0.0
            wins = 0.0
            for game in team:
                if game != '.':
                    gamesplayed = gamesplayed + 1.0
                if game == '1':
                    wins = wins + 1.0
            wp = wins / gamesplayed
            totalowp = 0.0
            numteams = 0.0
            for subix, subteam in enumerate(tourn):
                gamesplayed = 0.0
                wins = 0.0
                if index != subix and subteam[index] != '.':
                    numteams = numteams + 1.0
                    for gamenum, game in enumerate(subteam):
                        if gamenum != index:
                            if game != '.':
                                gamesplayed = gamesplayed + 1.0
                            if game == '1':
                                wins = wins + 1.0
                    totalowp = totalowp + (wins / gamesplayed)
            owp = totalowp / numteams
            teamresults.append(wp)
            teamresults.append(owp)
            results.append(teamresults)
        for ix, result in enumerate(results):
            oowptotal = 0.0
            oowpteams = 0.0
            for iy, subres in enumerate(results):
                if ix != iy and tourn[ix][iy] != '.':
                    oowpteams = oowpteams + 1.0
                    oowptotal = oowptotal + subres[1]
            result.append(oowptotal/oowpteams)
        
        fo.write("Case #" + str(count+1) + ":\n")
        for result in results:
            overallresult = (0.25 * result[0]) + (0.50 * result[1]) + (0.25 * result[2])
            fo.write(str(overallresult) + "\n")
        print count+1
            

if __name__ == '__main__':
    main()