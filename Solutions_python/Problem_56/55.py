infile = file("A-large.in")


def read_board(N):
    return [list(infile.readline().strip()) for row in xrange(N)]

def print_board(B):
    print "\n".join(["".join(R) for R in B])

def apply_gravity(board):
    for row_ix in xrange(len(board)):
        board[row_ix] = apply_row_gravity(board[row_ix])

def apply_row_gravity(r):
    L = len(r)
    r = [c for c in r if c != '.']
    r = ['.'] * (L - len(r)) + r
    return r

def run_case(case_num):
    N, K = map(int, infile.readline().strip().split())
    #print (N,K)
    board = read_board(N)
    #print_board(board)
    apply_gravity(board)
    #print_board(board)
    winner = find_winner(board, K)
    print "Case #%d: %s" % (case_num, winner)


class CellInfo:
    def __init__(self):
        self.W = 0
        self.N = 0
        self.NW = 0
        self.NE = 0 # !!!

    def is_winner(self, needed):
        if self.W + 1 >= needed:
            return True
        if self.N + 1 >= needed:
            return True
        if self.NW + 1 >= needed:
            return True
        if self.NE + 1 >= needed:
            return True

def update_cellinfo(ch, cellinfo, row, prev_row, cellrow, prev_cellrow, x):
            if row[x] == ch:
                if x > 0:
                    if row[x-1] == ch:
                        cellinfo.W = cellrow[x-1].W + 1
                if prev_cellrow:
                    if prev_row[x] == ch:
                        cellinfo.N = prev_cellrow[x].N + 1
                    if x > 0:
                        if prev_row[x-1] == ch:
                            cellinfo.NW = prev_cellrow[x-1].NW + 1
                
def update_cellinfo_again(ch, cellinfo, row, prev_row, cellrow, prev_cellrow, x):
            if row[x] == ch and x < len(row) - 1 and prev_cellrow:
                if prev_row[x+1] == ch:
                    cellinfo.NE = prev_cellrow[x+1].NE + 1
                
def find_winner(board, num_needed):
    cells = []
    prev_R_cellrow = None
    prev_B_cellrow = None
    prev_row = None

    R_cellinfos = []
    B_cellinfos = []
    
    R_wins = False
    B_wins = False
    
    
    for y in xrange(len(board)):
        row = board[y]
        R_cellrow = []
        B_cellrow = []
        for x in xrange(len(row)):
            if not R_wins:
                R_cellinfo = CellInfo()
                update_cellinfo('R', R_cellinfo, row, prev_row, R_cellrow, prev_R_cellrow, x)
                if R_cellinfo.is_winner(num_needed):
                    R_wins = True
                R_cellrow.append(R_cellinfo)
                    
            if not B_wins:
                B_cellinfo = CellInfo()
                update_cellinfo('B', B_cellinfo, row, prev_row, B_cellrow, prev_B_cellrow, x)
                if B_cellinfo.is_winner(num_needed):
                    B_wins = True
                B_cellrow.append(B_cellinfo)
                    
            if R_wins and B_wins:
                return "Both"
        R_cellinfos.append(R_cellrow)
        B_cellinfos.append(B_cellrow)

        prev_R_cellrow = R_cellrow
        prev_B_cellrow = B_cellrow
        prev_row = row
            
    if not R_wins or not B_wins:
        # Ok, we've tested | - \. We still need to test /
        prev_R_cellrow = None
        prev_B_cellrow = None
        prev_row = None
        for y in xrange(len(board)):
            row = board[y]
            R_cellrow = R_cellinfos[y]
            B_cellrow = B_cellinfos[y]
            for x in xrange(len(row)-1, -1, -1):
                if not R_wins:
                    R_cellinfo = R_cellrow[x]
                    update_cellinfo_again('R', R_cellinfo, row, prev_row, R_cellrow, prev_R_cellrow, x)
                    if R_cellinfo.is_winner(num_needed):
                        R_wins = True

                if not B_wins:
                    B_cellinfo = B_cellrow[x]
                    update_cellinfo_again('B', B_cellinfo, row, prev_row, B_cellrow, prev_B_cellrow, x)
                    if B_cellinfo.is_winner(num_needed):
                        B_wins = True
            
                if R_wins and B_wins:
                    return "Both"

            prev_R_cellrow = R_cellrow
            prev_B_cellrow = B_cellrow
            prev_row = row

    # We're done
    if R_wins and B_wins:
        return "Both"
    elif R_wins:
        return "Red"
    elif B_wins:
        return "Blue"
    else:
        return "Neither"



T = int(infile.readline())
for casenum in xrange(1, T+1):
    run_case(casenum)
