T = int(raw_input())

for t in xrange(T):
    winner = "RICHARD"

    x, r, c = map(int, raw_input().split())

    max_ = max(r, c)
    min_ = min(r, c)

    win = False
    if x > max_:
        win = True
    if (r==1 or c==1) and x > 2:
        win = True
    if x == 4 and min_ == 2:
        win = True
    if x == 5:
        win = True
    if x == 6:
        win = True
    if x >= 7:
        win = True
    if (x+1)/2 > min_:
        win = True

    board = r*c
    # have to use at least 1 copy that richard chose
    board -= x
    # can fill remaining board
    if win == False and board % x == 0:
        winner = "GABRIEL"

    print "Case #" + str(t+1) + ": " + winner
