# coding=utf-8
"""
Runs the code to utilise TicTacToeTomek.py
Expected Output:
Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
"""
__author__ = 'GPS'

from TicTacToeTomek import TicTacToeTomek


inp = f = open('input.dat', 'r')

num = int(f.readline().strip('\n'))

out = open('output.dat', 'w')

for i in range(num):
    if i > 0:
        out.write("\n")
    play = TicTacToeTomek(i + 1)
    play.board[0] = f.readline().strip('\n')
    play.board[1] = f.readline().strip('\n')
    play.board[2] = f.readline().strip('\n')
    play.board[3] = f.readline().strip()
    # print str(i + 1) + " :: " + str(play.board)
    res = play.result()
    if res == 1:
        # print "Case #%d: X won" % (i + 1)
        out.write("Case #%d: X won" % (i + 1))
    elif res == 2:
        # print "Case #%d: O won" % (i + 1)
        out.write("Case #%d: O won" % (i + 1))
    elif res == 3:
        # print "Case #%d: Draw" % (i + 1)
        out.write("Case #%d: Draw" % (i + 1))
    elif res == 0:
        # print "Case #%d: Game has not completed" % (i + 1)
        out.write("Case #%d: Game has not completed" % (i + 1))
    f.readline()

out.close()

f.close()