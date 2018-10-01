# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from __future__ import print_function

def get_fileinput():
    in_file = open("in", "r")
    cases = in_file.readline()
    
    out_file = open("out", "w")
    
    for i in range(int(cases)):
        out_file.write("Case #" + str(i+1) + ": ")
        out_file.write(str(find_numfriends(in_file.readline())) + "\n")
    
    in_file.close()
    out_file.close()

def find_numfriends(instr):
    sMax = instr[0]
    sTot = 0
    numfriends = 0
    sNext = int(instr[2])
    for k in range(int(sMax)):
        sTot = sTot + sNext
        sNext = int(instr[3+k])
        if sNext!=0:
            if sTot + numfriends < k+1:
                numfriends = k + 1 - sTot 
                
    return numfriends

__author__ = "ww"
__date__ = "$Apr 10, 2015 10:04:48 PM$"

get_fileinput()


