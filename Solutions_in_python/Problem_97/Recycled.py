'''
JamIt - Google Code Jam Scaffold Generator

Copyright (C) 2012 C. A. Cois

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.

----

Google Code Jam 2012
Problem: Recycled
Coder: C. A. Cois
'''
import jamit
from jamit import Case
from jamit import Solver
import sys
import time

#-----------------
# Jamit Scaffolds
#-----------------

class RecycledCase(Case):
    A = 0
    B = 0
    
    def populate(self, line):
        pair = line.split(' ')
        self.A = int(pair[0].strip())
        self.B = int(pair[1].strip())
        print("(" + str(self.A) + "," + str(self.B) + ")")
        return

    def isDone(self):
        ### You have to implement this
        return

    def __str__(self):
        ### You have to implement this
        return
		
class RecycledSolver(Solver):
    recycled = 0
    
    def __init__(self):
        ### You have to implement this
        return
    
    def solve(self, case):
        self.recycled = 0
        # for every value of m between A and B
        for m in range(case.A,case.B+1):
            # for every value of n between A and the current value of m
            for n in range(case.A,m):
                # if m and n have the same number of digits
                if len(str(m)) == len(str(n)) and len(str(n)) > 1:
                    # check if n and m are a recycled pair
                    if self.isRecycled(n,m):
                        self.recycled = self.recycled + 1
        return self.recycled

    def isRecycled(self, n, m):
        #print("Checking pair (" + str(n) + "," + str(m) + ")")
        # for each digit in n
        list_n = self.int_to_list(n)
        for i in range(0, len(str(n))-1):            
            #push one int from back to front
            cycled = list_n[len(list_n)-1:len(list_n)]
            cycled.extend(list_n[0:len(list_n)-1])
            int_n = self.list_to_int(cycled)
            #print("\tCycle " + str(i) + " of m = " + str(int_m) )
            #time.sleep(1)
            if int_n == int(m):
                #print("Match! (" + str(n) + "," + str(m) + ")")
                return True
            list_n = cycled
        return False

    def int_to_list(self, i):
        #print("Converting " + str(i) + " to string")
        return [int(x) for x in str(i)]

    def list_to_int(self, list):
        #print("Converting " + str(list) + " to int")
        return int("".join(str(x) for x in list))

#--------------
# Command Line
#--------------

if __name__ == "__main__":

    cases = []

    if len(sys.argv) < 2:
        print("Please supply an input data file")
        exit()
    
    # read in file from command line parameter
    filename = sys.argv[1]
    file = open(filename,"r")

    # parse input file into cases list
    file.readline() # ignore first line
    while file:
        line = file.readline()
        if line == '':
            break
        case = RecycledCase()
        case.populate(line)
        cases.append(case)
    
    file.close()

    # initialize solver
    solver = RecycledSolver()

    file = open("output.txt","w")

    # solve cases
    ctr = 1
    for case in cases:
        result = solver.solve(case)
        file.write("Case #" + str(ctr) + ": " + str(result) + "\n")
        ctr = ctr + 1

