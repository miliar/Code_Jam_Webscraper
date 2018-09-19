#!/usr/bin/env python

###### Modules ######
import os
import math
import string
import sys
import itertools
#####################

##########################################################################
working_dir = "C:\Users\srinidhihc\Downloads\\"
#input_file = "B-small-attempt2-chk.in"
#output_file = "B-small-attempt2-chk.out"

#input_file = "A_tst.in"
#output_file = "A_tst.out"
input_file = "A-small-attempt0.in"
output_file = "A-small-attempt0.out"
junk_file = "junk.txt"
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
    #n = int(in_file.readline())
    Rs, Cs, Ns = (in_file.readline()).split()
    R = int(Rs)
    C = int(Cs)
    N = int(Ns)
    return [R, C, N]
#****************************************************************
#***************************************************************
def Compute_Result(test_case):
    """ Grab a single testcase, perform computation and return the result."""
    R = test_case[0]
    C = test_case[1]
    N = test_case[2]
    res = 0
    if C%N:
        res = R * (N + C/N)
    else:
        res = R * (N + C/N - 1)


    return res
    #return int(math.floor((math.floor(math.log((float(P)/float(L)),C)))/float(2)))
        

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
        formatted_result = 'Case #' + str(case_index) + ': ' + str(result)
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
    # dictionary to store result of computation. Key = testcase#
    results ={}
    for index in range(T):
        test_case = Get_One_Test_Case(f)
        result = Compute_Result(test_case)
        case_index = index+1
        results[case_index] = result
        
    print "T = ", T
    abs_out_file_path = working_dir + output_file
    Save_And_Display_Results(results, abs_out_file_path)
    f.close()

#***************************************************************
if __name__ == '__main__':
    main()
    
