#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

#small practice
input_lines = open("B-small-attempt0.in").readlines()
input_lines = [int(x.replace("\n","")) for x in input_lines]



def valid_(value):
    x  = np.array(list(map(int,list(str(value)))))
    diff_  = np.diff(x)
    if len(np.where(diff_<0)[0])!=0:
        return False
    return True

    
test_cases = input_lines[1:]

out_ = open("quali_smallB.out","w")
for case_ in range(0,len(test_cases)):
    input_ = test_cases[case_]
    
    for i in range(input_,0,-1):
        if valid_(i):
            output_val = i
            break
       
    out_.write("Case #{}: {}\n".format(case_+1,output_val))
out_.close()   