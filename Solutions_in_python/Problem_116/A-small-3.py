#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
Google Cod Jam
Tic Tac Toe Tomek
https://code.google.com/codejam/contest/2270488/dashboard
"""

import sys
import os
import traceback
import argparse
import time
import re
from CodeJam import CodeJam

#from pexpect import run, spawn

def debug(*vals, **kwargs):
    global args
    if args.verbose:
        print(*vals, **kwargs)

class TicTacToe(CodeJam):

    results = {
        'X' : 'X won',
        'D' : 'Draw',
        '.' : 'Game has not completed',
        'O' : 'O won'
    }

    def check(self):
        notDone = False
        grid = self.grid[:]

        for i in range(2):
            # check horizontals
            for row in grid:
                result = self.checkSet(set(row))
                if result == '.' : # empty slots
                    notDone = True
                elif result in ['X', 'O']:
                    return result
            grid = list(zip(*grid)) # transpose grid

        # check diagonals
        l = 4
        print(grid)
        leftDiag = set([grid[i][i] for i in range(l)] )
        result = self.checkSet(leftDiag)
        if result == '.' : # empty slots
            notDone = True
        elif result in ['X', 'O']:
            return result
        rightDiag = set( [grid[l-1-i][i] for i in range(l-1,-1,-1)])
        result = self.checkSet(rightDiag)
        if result == '.' : # empty slots
            notDone = True
        elif result in ['X', 'O']:
            return result

        # either not done, or not draw
        return "." if notDone else "D"

    def checkSet(self,theSet):
        if '.' in theSet: # empty slots
            return '.'
        if 'O' in theSet and 'X' in theSet: # no good
            return 'D'
        if 'O' in theSet: # O won
            return 'O'
        if 'X' in theSet: # X won
            return 'X'

    def addGrid(self, elements):
        self.grid=elements

    def getResults(self):
        return self.results[self.check()]

    def run(self):
        board = []
        boardCount = 0
        for lineNum, line in self.getInput():
            if lineNum== 0:
                total = int(line)
                continue
            if line != "":
                board.append(list(line))
            if len(board) == 4:
                self.addGrid(board)
                boardCount += 1
                result = self.getResults()
                self.writeOutput(boardCount,result)
                board = []

        if boardCount != total:
            print("ERROR: Expected %d, got %d boards" % (total,boardCount))



def main():

    global args
    # TODO: Do something more interesting here...
    t=TicTacToe('A-large')

    t.addGrid([
        list("XXOT"),
        list("XOO."),
        list("XOO."),
        list("XO..")
        ])
    print(t.getResults())
    t.addGrid([
        list("OXOT"),
        list("XOO."),
        list("XOO."),
        list("XO.O")
        ])
    print(t.getResults())
    t.addGrid([
        list("OXOT"),
        list("XOXX"),
        list("XOOO"),
        list("OOXX")
        ])
    print(t.getResults())

    t.run()

    # case = 1
    # for linenum, line in iter(c.getInput()):
    #     if linenum == 0:
    #         continue
    #     lineMod = linenum % 3
    #     if lineMod == 0:
    #         prices=line.split(' ')
    #         result = c.process(credit,items,prices)
    #         c.writeOutput(case, "%d %d" % (result[0],result[1]))
    #         case += 1
    #     elif lineMod == 1:
    #         credit=int(line)
    #     else:
    #         items = line

if __name__ == '__main__':
    try:
        start_time = time.time()
        # Parser: See http://docs.python.org/dev/library/argparse.html
        parser = argparse.ArgumentParser(description='Python script')
        parser.add_argument('-v', '--verbose', action='store_true', default=False, help='verbose output')
        parser.add_argument('-ver', '--version', action='version', version='1.0')
        args = parser.parse_args()
        debug(time.asctime())
        main()
        debug(time.asctime())
        debug("Total time in seconds: ", end="")
        debug((time.time() - start_time))
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        traceback.print_exc()
        os._exit(1)

