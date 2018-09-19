'''
Created on Apr 8, 2013
This file is imported in all codejam source files
@author: kon
'''

import os
def print_case(f, i, s):
    f.write("Case #%d: %s\n" %(i,s))
    
def print_file(folder, filename, solutions):
    filename = os.getcwd() + os.sep + folder + os.sep + filename
    
    f = open(filename, 'w')
    for i,sol in enumerate(solutions): 
        print_case(f, i+1, sol)
    f.close()
        
def get_input_file(folder, filename):
    input_file = os.getcwd() + os.sep + folder + os.sep + filename
    f = open(input_file, 'r')
    return f

def solve(infile, func):
    folder = 'resources'
    solutions = func(get_input_file(folder, infile))
    outfile = infile.replace('.in','.out')
    print_file(folder, outfile, solutions)