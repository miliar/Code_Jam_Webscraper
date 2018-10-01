import os
import random
import re
import time,math,random,sys

path = "D:/Download/"
inputs = []
nbrInputs = -1
output_string = ""

# Open the input
with open(path + 'A-large.in') as data_file:
    content = data_file.readlines()

    for entry in content:
        if nbrInputs == -1:
            nbrInputs = int(entry)
        else:
            case = []
            caseStr = entry.split()
            count = int(caseStr[0])
            for c in caseStr[1]:
                case.append(int(c))

            inputs.append(case)
print("Inputs loaded: " + str(len(inputs)))


def resolve(case, indexcase):
    somme = 0
    friends = 0

    for i in range(len(case)):
        adding = i-somme
        if adding > 0:
            friends += adding
            somme += adding

        somme += case[i]
    return "Case #"+str(indexcase+1)+": " + str(friends)


# Resolve and output to file
for i in range(len(inputs)):
    output_string += resolve(inputs[i], i)
    if i != len(inputs)-1:
        output_string += "\n"

f = open('D:/Download/output', 'w')
f.write(output_string)
f.close()