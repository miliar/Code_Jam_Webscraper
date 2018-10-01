import sys

def joink():

    f = open("A-large.in", "r")

    T = int(f.readline())

    #for testNum in range(1, 5):
    for testNum in range(1, T+1):
        n, k = map(int, f.readline().split())

        game = []
        for i in range(n):
            line = f.readline().strip().replace('.', '').rjust(n, '.')
            game.append(line)
            #print 'game', game[i]
            
        winner = get_winner(game, k, n)
        print "Case #%d: %s" % (testNum, winner) 

def get_winner(game, k, n):
    """ Returns Neither, Both, Red or Blue.

    get_winner(lst<str>) -> str
    """
    winners = set()
    directions = ((0, 1), (1,1), (1, 0), (1, -1), (0, -1),
                  (-1, -1), (-1, 0), (-1, 1))
    for r in range(n):
        for c in range(n):
            curr = game[r][c]
            if curr != '.' and curr not in winners:
                going = True
                for dire in directions:
                    count = 1
                    rn, cn = r, c

                    rn += dire[0]
                    cn += dire[1]

                    while in_map(rn, cn, n):
                        if game[rn][cn] != curr:
                            break
                        count += 1
                        if count == k:
                            winners.add(curr)
                            going = False
                            break
                        rn += dire[0]
                        cn += dire[1]
                        
                    if not going:
                        break

    if len(winners) == 0:
        return "Neither"
    if len(winners) == 2:
        return "Both"
    if "R" in winners:
        return "Red"
    return "Blue"

def in_map(r, c, n):
    return 0 <= r < n and 0 <= c < n

joink()

