#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def main(argv=None):
    if len(argv)<1:
        print "Please specify input file"
        return 1
    fh = open(argv[0], 'rt')
    line = fh.readline().strip()
    T = int(line)
    for i in range(T):
        board=[]
        for j in range(4):
            board.append(fh.readline().strip())
        fh.readline()
	#add reverse board
	for j in range(4):
	    board.append("".join([board[0][j],board[1][j],board[2][j],board[3][j]]))
        #add diagonal
        board.append("".join([board[0][0],board[1][1],board[2][2],board[3][3]]))
        board.append("".join([board[0][3],board[1][2],board[2][1],board[3][0]]))
        #print board
        # examine board
        done=False
        completed=True
        for line in board:
            if re.search("OOOO",line.replace("T","O")):
                print "Case #%d: O won"%(i+1)
		done=True
		break
            if re.search("XXXX",line.replace("T","X")):
                print "Case #%d: X won"%(i+1)
                done=True
                break
	    if line.find(".")>-1:
                completed=False
        if done:
            continue
	if not completed:
	    print "Case #%d: Game has not completed"%(i+1)
	else:
	    print "Case #%d: Draw"%(i+1)
    fh.close()



if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

