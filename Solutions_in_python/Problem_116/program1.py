import sys

input_file_name = 'input1.txt'
output_file_name = 'output1.txt'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

contents = f_in.readlines()

num_cases = int(contents.pop(0))

WinnerString = ['O won','X won','Draw','Game has not completed']

for case_num in range(num_cases):

    matrix = [[0 for x in range(4)] for y in range(4)] 
    for i in range(4):
        row = contents.pop(0)   
        letters = list(row)
        for j in range(4):
            matrix[i][j] = letters[j]

    if case_num < (num_cases - 1):
        contents.pop(0)

    WinnerCode = -1
    OWins = 0
    XWins = 1
    Draw = 2
    NotComplete = 3

    NumDot = 0

    #Check Rows
    for i in range(4):
        NumX = 0
        NumO = 0
        NumT = 0
        for j in range(4):
            if (matrix[i][j] == 'X'):
                NumX = NumX + 1
            if (matrix[i][j] == 'O'):
                NumO = NumO + 1
            if (matrix[i][j] == 'T'):
                NumT = NumT + 1
            if (matrix[i][j] == '.'):
                NumDot = NumDot + 1
        if (NumX == 4) or ((NumX == 3) and (NumT == 1)):
            WinnerCode = XWins
            break
        elif (NumO == 4) or ((NumO == 3) and (NumT == 1)):
            WinnerCode = OWins
            break
        else:
            pass

    if (WinnerCode == -1):
    #Check Cols
        for j in range(4):
            NumX = 0
            NumO = 0
            NumT = 0
            for i in range(4):
                if (matrix[i][j] == 'X'):
                    NumX = NumX + 1
                if (matrix[i][j] == 'O'):
                    NumO = NumO + 1
                if (matrix[i][j] == 'T'):
                    NumT = NumT + 1
                if (matrix[i][j] == '.'):
                    NumDot = NumDot + 1
            if (NumX == 4) or ((NumX == 3) and (NumT == 1)):
                WinnerCode = XWins
                break
            elif (NumO == 4) or ((NumO == 3) and (NumT == 1)):
                WinnerCode = OWins
                break
            else:
                pass

    if (WinnerCode == -1):
    #Check Diag1
        NumX = 0
        NumO = 0
        NumT = 0
        for i in range(4):
            if (matrix[i][i] == 'X'):
                NumX = NumX + 1
            if (matrix[i][i] == 'O'):
                NumO = NumO + 1
            if (matrix[i][i] == 'T'):
                NumT = NumT + 1
        if (NumX == 4) or ((NumX == 3) and (NumT == 1)):
            WinnerCode = XWins
        elif (NumO == 4) or ((NumO == 3) and (NumT == 1)):
            WinnerCode = OWins
        else:
            pass

    if (WinnerCode == -1):
    #Check Diag2
        j=3
        NumX = 0
        NumO = 0
        NumT = 0
        for i in range(4):
            if (matrix[i][j] == 'X'):
                NumX = NumX + 1
            if (matrix[i][j] == 'O'):
                NumO = NumO + 1
            if (matrix[i][j] == 'T'):
                NumT = NumT + 1
            j = j - 1
        if (NumX == 4) or ((NumX == 3) and (NumT == 1)):
            WinnerCode = XWins
        elif (NumO == 4) or ((NumO == 3) and (NumT == 1)):
            WinnerCode = OWins
        else:
            pass

    if (WinnerCode == -1):
        if (NumDot > 0):
            WinnerCode = NotComplete
        else:
            WinnerCode = Draw
            
#    print('Case #{}: {}'.format(case_num + 1, WinnerString[WinnerCode]))
    print('Case #{}: {}'.format(case_num + 1, WinnerString[WinnerCode]), file = f_out)   
    
f_in.close()
f_out.close()
