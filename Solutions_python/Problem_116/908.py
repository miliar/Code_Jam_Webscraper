import sys
f= open(sys.argv[1])
cases = int(f.readline())
of = open(sys.argv[2],'w')
for case in xrange(1,cases+1):
    board_rows = []
    board_cols = [[],[],[],[]]
    result = "Draw"
    diag_1 = []
    diag_2 = []
    for i in xrange(0,4):
        line = f.readline()
        if '.' in line:
            result = "Game has not completed"
        diag_1.append(line[i])        
        diag_2.append(line[3-i])
        for j in xrange(0,4):
            board_cols[j].append(line[j])
        board_rows.append([j for j in line if j!='\n'])
    states = [board_rows,board_cols,[diag_1,diag_2]]
    for state in states:
        for line in state:
            if line.count('X') + line.count('T') == 4:
                result = "X won"
            if line.count('O') + line.count('T') == 4:
                result = "O won"
    of.write("Case #%s: %s\n"%(case,result))
    f.readline()
