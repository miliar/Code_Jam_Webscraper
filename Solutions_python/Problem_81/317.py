#!/usr/bin/env python

if __name__ == '__main__':
    from sys import stdin

    lines = stdin.readlines()

    T = int(lines[0])
    l = 1 # next working line
    for t in range(1,T+1):
        # parse case data
        N = int(lines[l])
        l += 1
        schedule = [lines[l+i][:N] for i in range(N)]
        l += N

        # calculate WP
        wp = []
        wins = []
        lose = []
        play = []
        for i in range(N):
            nwins = 0
            nlose = 0
            for j in range(N):
                if schedule[i][j] == '1':
                    nwins += 1
                if schedule[i][j] == '0':
                    nlose += 1
            nplay = nwins + nlose
            play.append(nplay) 
            wins.append(nwins)
            lose.append(nlose)
            # if i hasn't played a game, then i has won all games
            ratio = 1.0
            if nplay != 0:
                ratio = float(nwins)/nplay
            wp.append(ratio)

        # calculate OWP
        owp = []
        for i in range(N):
            Swp = 0.0
            for j in range(N):
                if schedule[i][j] != '.':
                    nwins = wins[j] - (schedule[i][j] == '0')
                    nplay = play[j] - 1
                    # if j has only played against i, then he won
                    # all his other games (since there are no other games)
                    ratio = 1.0
                    if nplay != 0:
                        ratio = float(nwins)/nplay
                    Swp += ratio
            owp.append(Swp / play[i])

        # calculate OOWP
        oowp = []
        for i in range(N):
            Sowp = 0
            for j in range(N):
                if schedule[i][j] != '.':
                    Sowp += owp[j]
            # if i hasn't had any opponents, then all of i's opponents
            # have a perfect score
            ratio = 1.0
            if play[i] != 0:
                ratio = Sowp / play[i]
            oowp.append(ratio)

        # output results
        print("Case #{0}:".format(t))
        for i in range(N):
            rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]
            print(rpi)

    
