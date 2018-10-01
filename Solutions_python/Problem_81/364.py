import numpy

def calc_rpi(wins, games):

    N = len(wins)
    
    total_games = numpy.sum(games, 1)
    total_wins = numpy.sum(wins, 1)

    wp = total_wins / total_games

    wins_without = (total_wins[None, :] - wins.T)
    wins_without[numpy.eye(N, dtype = bool)] = 0
    games_without = (total_games[None, :] - games.T)
    owp_mat = (wins_without / games_without) * games
    
    owp = numpy.sum(owp_mat, 1) / total_games

    oowp = numpy.sum(games * owp, 1) / total_games
    
    return 0.25 * wp + 0.5 * owp + 0.25 * oowp
    
def solve_A(infile, outfile):
    lines = open(infile).readlines()
    T = int(lines[0])
    cur = 1
    res = []
    
    for i in xrange(T):
        N = int(lines[cur])
        cur += 1
        wins = numpy.zeros((N, N))
        games = numpy.ones((N, N))
        for j in range(N):
            for k in range(N):
                if lines[cur][k] == "1":
                    wins[j,k] = 1
                elif lines[cur][k] == ".":
                    games[j,k] = 0
            cur += 1
        rpi = calc_rpi(wins, games)
        res.append("Case #%d:" % (i + 1))
        res.extend(map(str, rpi))
    open(outfile, "w").write("\n".join(res))
