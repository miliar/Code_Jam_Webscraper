#!/usr/bin/python
# magictrick.py - Sumit Mahamuni


import sys

filename = sys.argv[1]

with open(filename) as file:
    numberOfTestCases = int(file.readline())
    for example in range(1,numberOfTestCases+1):
	first_answer = int(file.readline());
        for i in range(1, 5):
            if(i == first_answer):
                first_set = set(file.readline().strip().split(' '))
            else:
		file.readline()
        
        second_answer = int(file.readline())
        
        for i in range(1, 5):
            if i == second_answer:
                second_set = set(file.readline().strip().split(' '))
            else:
		file.readline()
        
        intersection = first_set.intersection(second_set)
        
	if len(intersection) == 0:
            print "Case #"+str(example)+": Volunteer cheated!"
        elif len(intersection) == 1:
            print "Case #"+str(example)+":",intersection.pop()
        else:
            print "Case #"+str(example)+": Bad magician!"
