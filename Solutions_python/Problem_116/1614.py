def analyze(input):
    lines = input.split('\n')
    boards = int(lines[0])

    for i in range(boards):
        curr_board = lines[(i*5)+1:(i*5)+5]
        values = {}
        for j in range(4):
            for k in range(4):
                piece = curr_board[j][k]
                if "row_"+str(j)+"_"+piece not in values:
                    values["row_"+str(j)+"_"+piece] = 0
                if "col_"+str(k)+"_"+piece not in values:
                    values["col_"+str(k)+"_"+piece] = 0
                if "diag1_"+piece not in values:
                    values["diag1_"+piece] = 0
                if "diag2_"+piece not in values:
                    values["diag2_"+piece] = 0
                values["row_"+str(j)+"_"+piece] += 1
                values["col_"+str(k)+"_"+piece] += 1
                if j == k:
                    values["diag1_"+piece] += 1
                if j+k == 3:
                    values["diag2_"+piece] += 1
                
        is_full = True

        for q in range(4):
            for piece in "XOT.":
                if "row_"+str(q)+"_"+piece not in values:
                    values["row_"+str(q)+"_"+piece] = 0
                if "col_"+str(q)+"_"+piece not in values:
                    values["col_"+str(q)+"_"+piece] = 0
                if "diag1_"+piece not in values:
                    values["diag1_"+piece] = 0
                if "diag2_"+piece not in values:
                    values["diag2_"+piece] = 0

        result = ""
        for l in range(4):
            if (values["row_"+str(l)+"_"+"."] != 0) or (values["col_"+str(l)+"_"+"."] != 0):
                is_full = False
            if (values["row_"+str(l)+"_"+"X"] + values["row_"+str(l)+"_"+"T"] == 4) or (values["col_"+str(l)+"_"+"X"] + values["col_"+str(l)+"_"+"T"] == 4):
                result = "X won"
                break
            if (values["row_"+str(l)+"_"+"O"] + values["row_"+str(l)+"_"+"T"] == 4) or (values["col_"+str(l)+"_"+"O"] + values["col_"+str(l)+"_"+"T"] == 4):
                result = "O won"
                break
         
        
        if (values["diag1_X"] + values["diag1_T"] == 4) or (values["diag2_X"] + values["diag2_T"] == 4):
            result = "X won"
        elif (values["diag1_O"] + values["diag1_T"] == 4) or (values["diag2_O"] + values["diag2_T"] == 4):
            result = "O won"
        elif is_full and result == "":
            result = "Draw"
        elif result == "":
            result = "Game has not completed"

        print "Case #"+str(i+1)+": "+result
         
input = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O"""

input2 = """10
XXOO
OOXX
XOOT
XXOX

O.X.
.OO.
XXO.
XX.O

X.O.
OOOO
XTX.
.X.X

....
OOX.
X.OT
..XX

OXXX
O...
O...
T...

XO..
XTXX
XO.O
X.OO

X...
X.O.
X.O.
X.O.

XTOX
OOOX
XOXX
OXOX

....
....
....
....

XOOX
XXXO
OXXO
OOXO"""

