#!/usr/bin/env python

import sys


def ominus_game(N, row, col, player_names):
    assert len(player_names) == 2
    #print "\n", N, row, col
    longest_side = max(row, col)
    shortest_side = min(row, col)

    if N >= longest_side + 1: #first player can choose a N-size that doesn't fit into the grid
        #print "blocco fuori lato lungo"
        return player_names[0]
    if N >= (shortest_side + 1)* 2 - 1:  #first player can choose a N-size that doesn't fit into the grid
        #print "blocco fuori lato corto"
        return player_names[0]
    if N >= 8 and shortest_side >= 3: #first player can build a block with a hole inside smaller than N
        #print "blocco con buco"
        return player_names[0]
    if (row*col % N) != 0: #no way the second player can fill the grid with N-size blocks
        #print "non multiplo"
        return player_names[0]
    if shortest_side > 1 and N != row * col and N >= shortest_side  * 2 :  #first player can choose a valid block that divides the grid
        #print "divisione griglia"
        return player_names[0]


    #print "vincita possibile"
    return player_names[1]



def main():
    if len(sys.argv) < 2:
        print  "no filename specified"
        sys.exit(0)
    with open(sys.argv[1], "r") as f:
        t = int(f.readline()) #number of test cases
        for test in range(t):

            X,R,C = map(int, f.readline().split())
            print "Case #%d: %s" % (test+1, ominus_game(X, R, C, ["RICHARD", "GABRIEL",]))




if __name__ == '__main__':
    main()
