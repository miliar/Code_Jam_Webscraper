import re
import sys

def solve_board(infile):
    squares = ""
    for i in range(4):
        squares += infile.readline().strip()
    infile.readline()
    interesting_substrings = [squares[:4],
                              squares[4:8],
                              squares[8:12],
                              squares[12:],
                              "".join((squares[0],squares[4],squares[8],squares[12])),
                              "".join((squares[1],squares[5],squares[9],squares[13])),
                              "".join((squares[2],squares[6],squares[10],squares[14])),
                              "".join((squares[3],squares[7],squares[11],squares[15])),
                              
                              "".join((squares[0],squares[5],squares[10],squares[15])),
                              "".join((squares[3],squares[6],squares[9],squares[12]))
                              ]
    for s in interesting_substrings:
        ans = checkForWin(s)
        if ans is not None:
            return ans
    if squares.find('.') == -1:
        return "Draw"
    else:
        return "Game has not completed"
                     
    
def checkForWin(string):
    xcount = 0
    ocount = 0
    tcount = 0
    for letter in string:
        if letter == "X":
            xcount += 1
        elif letter == "O":
            ocount += 1
        elif letter == "T":
            tcount += 1
    if xcount == 4 or (xcount == 3 and tcount == 1):
        return "X won"
    if ocount == 4 or (ocount == 3 and tcount == 1):
        return "O won"
    return None
    #x wins if 4X or 3X and T
    #o wins if 4O or 3O and T
    #else either tie or in progress

if __name__=="__main__":
    infile = open(sys.argv[1],'r')
    outfile = open('output','w')
    
    t = int(infile.readline().strip())
    for i in range(t):
        result = solve_board(infile)
        string = "Case #%d: %s\n" % (i+1, result)
        print string
        outfile.write(string)
