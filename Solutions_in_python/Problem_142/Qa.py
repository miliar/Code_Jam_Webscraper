'''
Created on May 3, 2014

@author: Andrew
'''
import math
from itertools import groupby
import statistics
from collections import OrderedDict
with open("google.in", "r") as infile, open("solution.txt", "w") as outfile:
    cases = int(infile.readline())
    for case in range(0,cases):
        counter = 0
        stringamount = int(infile.readline())
        string = []
        for s in range(0,stringamount):
            s = infile.readline().strip()
            string.append(["".join(grp) for num, grp in groupby(s)])
        for numb in range(0,len(string[0])):
            temp = []
            if len(string[0]) != len(string[1]):
                counter = "Fegla Won"
                break;
            for num in range(0,stringamount):
                temp.append(string[num][numb])
            if temp[0][0] != temp[1][0]:
                counter = "Fegla Won"
                break;
            temp2 = []
            for thing in temp:
                temp2.append(len(thing))
            median = statistics.median_low(temp2)
            for number in temp2:
                counter += abs(number-median)             
        outfile.write("Case #" + str(case+1) + ": " + str(counter) + "\n")