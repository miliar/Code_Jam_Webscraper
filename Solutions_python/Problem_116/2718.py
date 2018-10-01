#!/usr/bin/env python

if __name__ == "__main__":
    loop = range(4)
    wins = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
               [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
               [0, 5, 10, 15], [3, 6, 9, 12]]
    for case in xrange(input()):
        # Take Input
        board = []
        for i in loop:
            board.append(list(raw_input()))
        raw_input()
        win = False
        # Check for win
        for c in wins:
            x = 0
            o = 0
            t = 0
            for idx in c:
                ch = board[idx/4][idx%4]
                if ch == 'X':
                    x += 1
                elif ch == 'O':
                    o += 1
                elif ch == 'T':
                    t += 1
            if (x==3 and t==1) or x==4:
                print 'Case #{0}: X won'.format(case+1)
                win = True
                break
            elif (o==3 and t==1) or o==4:
                print 'Case #{0}: O won'.format(case+1)
                win = True
                break
        if win:
            continue
        # Check for draw / nc
        dot = 0
        for i in range(15):
            ch = board[i/4][i%4]
            if ch == '.':
                dot += 1
        if dot > 0:
            print 'Case #{0}: Game has not completed'.format(case+1)
        else:
            print 'Case #{0}: Draw'.format(case+1)


