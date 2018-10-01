#!/usr/bin/env python
import sys

num_cases = -1

fileIN = open(sys.argv[1], "r")

num_cases = int(fileIN.readline())

for case_num in range(num_cases):
    outstring = ""
    values = [int(x) for x in fileIN.readline().split()]
    per_key = values[0]
    num_keys = values[1]
    num_letters = values[2]
    
    if num_letters > per_key * num_keys:
        fileIN.readline()
        outstring = "IMPOSSIBLE"
    
    else:
        values = [int(x) for x in fileIN.readline().split()]
        keypresses = 0
        
        values.sort()
        values.reverse()

        for i in range(per_key):
            for j in range(num_keys):
                if values:
                    value = values.pop(0)
                    keypresses += value * (i + 1)
                
        outstring = str(keypresses)

    

    sys.stdout.write("Case #" + str(case_num+1) + ": " + outstring + "\n")
