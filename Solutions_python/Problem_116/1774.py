#!/usr/bin/env python

###### Modules ######
import os
import math
import string
import sys
#####################

##########################################################################
working_dir = "C:\Users\MyPC\Documents\codejam_2013\Tic-Tac-Toe-Tomek-Qual-2013\\"
input_file = "A-large.in"
output_file = "A-large.out"
##########################################################################

#***************************************************************
def Grab_Input_File(working_dir, input_file):
    """ Input: working directory and input file name.
        Output: open input file and return file object. """
    abs_in_file_path = working_dir + input_file
    try:
        f = open(abs_in_file_path, 'rU')
    except IOError:
        print "Error: File not found"
        return 0
    return f
#****************************************************************
def Get_One_Test_Case(in_file):
    """ Extract one test case from the input file and
        put it in appropriate data structure.
        Input: file object, Output: a data structure containing single test case."""
    Mat = []
    for count in range(4):
        A = in_file.readline()
        B = A.split()
        C = B[0]
        #print C
        Mat.append(C)
    #print Mat
    #sys.exit(1)
    #print N
    #print  "***************"
    #print M
    #print "****************"
    #print Mat
    #sys.exit(1)
    return [Mat]
#****************************************************************
def bounds(C):
    """Swap x and y coordinates. """
    if C < 0:
        return 0
    else:
        return C
#***************************************************************
def Compute_Result(test_case, T):
    """ Grab a single testcase, perform computation and return the result."""
    Mat = test_case[0]
    Square = []
    for cnt in range(4):
        Square.append([1000, 1000, 1000, 1000])
    symbol_2_number = {}
    symbol_2_number["."] = 1000
    symbol_2_number["T"] = 0
    symbol_2_number["X"] = 1
    symbol_2_number["O"] = 100
    x_count = 0
    o_count = 0
    dot_flag = 0
    for i in range(4):
        for j in range(4):
            Square[i][j] = symbol_2_number[Mat[i][j]]
            if Mat[i][j] == "X":
                x_count+=1
            if Mat[i][j] == "O":
                o_count+=1
            if Mat[i][j] == ".":
                dot_flag = 1
    print "************"
    print Square
    print "***********"
    row_sum = [0, 0, 0, 0]
    col_sum = [0, 0, 0, 0]
    diag_sum = [0, 0]
    game_flag = -1
    for i in range(4):
        row_sum[i] = sum(Square[i][:])
    for i in range(4):
        for j in range(4):
            col_sum[i]+=Square[j][i]
    print "col_sum is:", col_sum
    d_sum = 0
    offdiag_sum = 0
    for i in range(4):
        d_sum+= Square[i][i]
        offdiag_sum+= Square[i][3-i]
    diag_sum[0] = d_sum
    diag_sum[1] = offdiag_sum
    sum_list = []
    sum_list.extend(row_sum)
    sum_list.extend(col_sum)
    sum_list.extend(diag_sum)
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    print sum_list
    print "x_count = ", x_count
    print "o_count = ", o_count
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    ret_code = "Draw"
    for element in sum_list:
        #print "elem = ", element
        if (element==3) or (element==4):
            ret_code = "X won"
            game_flag = 1
        elif (element == 300) or (element== 400):
            ret_code = "O won"
            game_flag = 1
        else:
            game_flag = game_flag
    if(dot_flag==1)& (game_flag!=1):
        ret_code = "Game has not completed"
            
    
    return ret_code    
        

#***************************************************************
def Save_And_Display_Results(results, output_file):
    """ Save the results into a specified output file and
        display the results on the screen."""
    def Format_Result(case_index, result):
        """ Returns the result transformed into one big string with
            new lines inserted at appropriate places. This string
            can be directly written into a file and also printed
            directly to screen."""
        ### Code to transform result into one big string.
        formatted_result = 'Case #' + str(case_index) + ': ' + result
        return formatted_result
    
    f = open(output_file, 'w')
    for case_index in sorted(results.keys()):
        formatted_result_to_screen = Format_Result(case_index, results[case_index])
        formatted_result_to_file = formatted_result_to_screen + '\n'
        f.write(formatted_result_to_file)
        print '***************************************'
        print formatted_result_to_screen
    print '***************************************'
    
#***************************************************************
def main():
    f = Grab_Input_File(working_dir, input_file)
    # Extract the number of test cases.
    T = int(f.readline())
    #print T
    #sys.exit(1)
    # dictionary to store result of computation. Key = testcase#
    results ={}
    for index in range(T):
        case_index = index + 1
        test_case = Get_One_Test_Case(f)
        junk = f.readline()
        #print test_case
        #print '*************************************'
        results[case_index] = Compute_Result(test_case, T)
    print "T = ", T
    abs_out_file_path = working_dir + output_file
    #sys.exit(1)
    Save_And_Display_Results(results, abs_out_file_path)
    f.close()

#***************************************************************
if __name__ == '__main__':
    main()
    