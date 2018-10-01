#!/usr/bin/python

import re
import sys
from string import maketrans

input_file = open('A-small-attempt1.in')
output_file = open('A-small.out', 'w')

T = int(input_file.readline())



trans = maketrans("qejmyslckdxvnribptahwfougz", 
                  "zoulangeismpbtdhrwyxfckjvq")

for t in range(T):

    result = input_file.readline().replace('\n','').translate(trans)
    output_file.write("Case #" + str(t + 1) + ": " + result + "\n")

input_file.close()
output_file.close()
