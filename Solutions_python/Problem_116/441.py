#!/usr/bin/env python
# Tic-Tac-Toe-Tomek
import sys

fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

def get_io(argv):
    fin = sys.stdin
    fout = sys.stdout
    ifn = ofn = "-"
    if len(argv) == 2:
        bfn = sys.argv[1]
        ifn = bfn + '.in'
        ofn = bfn + '.out'
    if len(argv) > 2:
        ifn = argv[1]
        ofn = argv[2]
    if ifn != '-':
        fin = open(ifn, "r")
    if ofn != '-':
        fout = open(ofn, "w")
    return (fin, fout)

def get_numbers():
    line = fin.readline()
    return map(int, line.split())

def get_number():
    return get_numbers()[0]

def get_line():
    line = fin.readline()
    if len(line) > 0 and line[-1] == '\n':
        line = line[:-1]
    return line

def get_string():
    line = fin.readline()
    return line.strip()


quads = []
slash = []
bslash = []
for i in range(4):
    row = []
    col = []
    slash.append((i, i))
    bslash.append((i, 3 - i))
    for j in range(4):
        row.append((i, j))
        col.append((j, i))
    quads.append(row)
    quads.append(col)
quads.append(slash)
quads.append(bslash)

# for q in quads:
#     sys.stderr.write("q=%s\n" % q)
# sys.exit(7)

class TicTacTowTomek:

    def __init__(self, lines):
        self.a = 4 * [None]
        for i in range(0, 4):
            self.a[i] = lines[i][:4]
        self.result = None
        self.judge()

    def judge(self):
        global quads
        qi = 0
        nq = len(quads)
        any_empty = False
        while self.result is None and qi < len(quads):
            self.check_quad(quads[qi])
            qi += 1
        if self.result is None:
            i = 0
            while self.result is None and i < 4:
                j = 0
                while self.result is None and j < 4:
                    if self.a[i][j] == '.':
                        self.result = "Game has not completed"
                    j += 1
                i += 1
            if self.result is None:
                self.result = "Draw"

    def check_quad(self, quad):
        x_won = o_won = True
        for xyi in range(4):
            i = quad[xyi][0] 
            j = quad[xyi][1]
            # self.log("xyi=%d, i=%d, j=%d" % (xyi, i, j))
            c = self.a[i][j]
            if c == '.':
                x_won = o_won = False
            elif c == 'X':
                o_won = False
            elif c == 'O':
                x_won = False
        if x_won:
            self.result = "X won"
        elif o_won:
            self.result = "O won"
                
            
    def log(self, msg):
        sys.stderr.write("%s\n" % msg)

    def log0(self, msg):
        pass
        

if __name__ == "__main__":
    (fin, fout) = get_io(sys.argv)
    n_cases = get_number()
    lines4 = 4*[None]
    for ci in range(n_cases):
        for i in range(4):
            lines4[i] = get_line()
        get_line() # empty
        tttt = TicTacTowTomek(lines4)
        fout.write("Case #%d: %s\n" % (ci + 1, tttt.result))

    fin.close()
    fout.close()
    sys.exit(0)

                   
