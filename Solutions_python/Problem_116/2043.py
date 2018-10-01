#!/usr/bin/python

# read the input file and store the contents in a variable
f = open("input.txt", "r")
content = f.readlines()
f.close()

# define the variables
test_case = 0
test_case_count = 0
test_case_line = 0
test_case_tmp = ""
cases = []
cases_wins = []

# process the file
for line in content:
    if test_case == 0:
        test_case_count = int(line)
        test_case = test_case + 1
        if test_case > 0:
            test_case_line = 1
    else:
        if test_case_line != 0:
            line = line.replace ("\n", "")
            
            if test_case_line != 4:
                line = line + "\n"
            
            test_case_tmp = test_case_tmp + line

            if test_case_line == 4:
                cases.append (test_case_tmp)
                test_case_tmp = ""
                test_case = test_case + 1
                test_case_line = 0
            else:
                test_case_line = test_case_line + 1
        else:
            test_case_line = test_case_line + 1

# determine the winner
for case in cases:   
    won = False
    case_original = case
    
    case = case.replace("T", "O")
    if "OOOO" in case:
        won = True
        cases_wins.append("O won")
    
    if not won:
        case = case_original
        case = case.replace("T", "X")
        if "XXXX" in case:
            won = True
            cases_wins.append("X won")
    
    if not won:
        case = case_original
        
        case = case.split("\n")
        
        vertical_case = case[0][0] + case[1][0] + case[2][0] + case[3][0]
        vertical_case = vertical_case + "\n" + case[0][1] + case[1][1] + case[2][1] + case[3][1]
        vertical_case = vertical_case + "\n" + case[0][2] + case[1][2] + case[2][2] + case[3][2]
        vertical_case = vertical_case + "\n" + case[0][3] + case[1][3] + case[2][3] + case[3][3]
        vertical_case_original = vertical_case
        
        vertical_case = vertical_case.replace("T", "O")
        if "OOOO" in vertical_case:
            won = True
            cases_wins.append("O won")
        
        if not won:
            vertical_case = vertical_case_original
            vertical_case = vertical_case.replace("T", "X")
            if "XXXX" in vertical_case:
                won = True
                cases_wins.append("X won")
                
    if not won:
        case = case_original
        
        case = case.split("\n")
        
        diagonal_case = case[0][0] + case[1][1] + case[2][2] + case[3][3]
        diagonal_case_original = diagonal_case
        
        diagonal_case = diagonal_case.replace("T", "O")
        if diagonal_case == "OOOO":
            won = True
            cases_wins.append("O won")
        
        if not won:
            diagonal_case = diagonal_case_original
            diagonal_case = diagonal_case.replace("T", "X")
            
            if diagonal_case == "XXXX":
                won = True
                cases_wins.append("X won")
                
    if not won:
        case = case_original
        
        case = case.split("\n")
        
        diagonal_case = case[0][3] + case[1][2] + case[2][1] + case[3][0]
        diagonal_case_original = diagonal_case
        
        diagonal_case = diagonal_case.replace("T", "O")
        if diagonal_case == "OOOO":
            won = True
            cases_wins.append("O won")
        
        if not won:
            diagonal_case = diagonal_case_original
            diagonal_case = diagonal_case.replace("T", "X")
            
            if diagonal_case == "XXXX":
                won = True
                cases_wins.append("X won")
                
    if not won:
        case = case_original
        
        if "." in case:
            cases_wins.append("Game has not completed")
        else:
            cases_wins.append("Draw")

# output the result
output = ""

for i in range(1, test_case_count + 1):
    output = output + "Case #" + str(i) + ": " + cases_wins[i - 1] + "\n"
    
f = open("output.txt", "w")
f.write(output)
f.close()