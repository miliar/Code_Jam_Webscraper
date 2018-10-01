__author__ = 'Ruben'

import copy

def did_symbol_win(board_local, symbol):
    #print "did_symbol_win of " + symbol + ":"
    board_local = copy.deepcopy(board_local)

    for y in xrange(4):
        for x in xrange(4):
            if board_local[y][x] == "T":
                board_local[y][x] = symbol

    for y in xrange(4):
        for x in xrange(4):

            if board_local[y][x] == symbol:
                starty = y
                endy = y

                while starty != 0 and board_local[starty-1][x] == symbol:
                    starty -= 1

                while endy != 3 and board_local[endy+1][x] == symbol:
                   endy += 1

                ystretch = endy - starty + 1

                startx = x
                endx = x

                while startx != 0 and board_local[y][startx-1] == symbol:
                    startx -= 1

                while endx != 3 and board_local[y][endx+1] == symbol:
                    endx += 1

                xstretch = endx - startx + 1

                #print "@", x, y, "|", ystretch, "and -", xstretch

                #\
                slide_br = 0
                slide_tl = 0

                while y+slide_br < 3 and x+slide_br < 3 and board_local[y+(slide_br+1)][x+(slide_br+1)] == symbol:
                    slide_br += 1

                while y-slide_tl > 0 and x-slide_tl > 0 and board_local[y-(slide_tl+1)][x-(slide_tl+1)] == symbol:
                    slide_tl += 1

                xystretch = slide_tl + slide_br + 1

                #/
                start_slide = 0
                end_slide = 0

                while y-start_slide > 0 and x+start_slide < 3 and board_local[y-(start_slide+1)][x+(start_slide+1)] == symbol:
                    start_slide += 1

                while y+end_slide < 3 and x-end_slide > 0 and board_local[y+(end_slide+1)][x-(end_slide+1)] == symbol:
                    end_slide += 1

                llur_stretch = end_slide + start_slide + 1

                if ystretch > 3:
                    return True

                if xstretch > 3:
                    return True

                if xystretch > 3:
                    return True

                if llur_stretch > 3:
                    return True

            pass

    return False

file = open("A-large.in")

cases = int(file.readline().strip())

for c in xrange(cases):
    c = c + 1
    board = [None] * 4
    board[0] = list(file.readline().strip())
    board[1] = list(file.readline().strip())
    board[2] = list(file.readline().strip())
    board[3] = list(file.readline().strip())

    if did_symbol_win(board, "X"):
        print "Case #" + str(c) + ": X won"
    elif did_symbol_win(board, "O"):
        print "Case #" + str(c) + ": O won"
    elif "." in ("".join(board[0])+"".join(board[1])+"".join(board[2])+"".join(board[3])):
        print "Case #" + str(c) + ": Game has not completed"
    else:
        print "Case #" + str(c) + ": Draw"

    #print board

    file.readline()







