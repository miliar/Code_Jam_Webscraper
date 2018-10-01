#!/usr/bin/env python3

import sys
from numpy import *

input_file = open(sys.argv[1], 'r')
output_file = open("out_" + sys.argv[0].rstrip(".py"), 'w')

input_size = int(input_file.readline().rstrip("\n"))



    


        
answers = [0,0]
lines = [0,0]
for i in range(input_size):
    output_file.write("Case #" + str(i + 1) + ": ")
    answers[0] = int(input_file.readline().rstrip("\n"))
    for i in range(4):
        if (i == answers[0] - 1):
            firstLine = list(map(int, input_file.readline().rstrip("\n").split()))
            print("First line, " + str(answers[0]) + ": " + str(firstLine) + "\n")
        else:
            input_file.readline()
    answers[1] = int(input_file.readline().rstrip("\n"))
    for i in range(4):
        if (i == answers[1] - 1):
            secondLine = list(map(int, input_file.readline().rstrip("\n").split()))
            print("Second line, " + str(answers[1]) + ": " + str(secondLine) + "\n")
        else:
            input_file.readline()
    possibleSolutions = set(firstLine).intersection(set(secondLine))
    print("Possible solutions : " + str(possibleSolutions))
    if (len(possibleSolutions) == 0):
        output_file.write("Volunteer cheated!\n")
    elif (len(possibleSolutions) > 1):
        output_file.write("Bad magician!\n")
    else:
        output_file.write(str(possibleSolutions.pop()) + '\n')

    
input_file.close()
output_file.close()
