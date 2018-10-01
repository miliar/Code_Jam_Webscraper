#!/usr/bin/python3
import sys

def main(name):

    fin = []
    with open(name, 'r') as f:
        fin = [x.rstrip() for x in f]

    num_cases = fin.pop(0)
    lines = [x.split() for x in fin]

    for line in lines:
        output(name, str(getNumFriends(line[1])))

    return 0

def getNumFriends(string):
    numThere = 0
    numNeeded = 0


    for i in range(len(string)):
        shyness = int(string[i])
        diff = i - numThere
        if diff > 0:
            numNeeded += diff
            numThere += diff + shyness
        numThere += shyness


    return numNeeded
first = True
case_num = 1
def output(name, line):
    global first
    global case_num

    if first:
        with open(name+".out", 'w') as f:
            f.write("Case #" + str(case_num) + ": " + line)
    else:
        with open(name + ".out", 'a') as f:
            f.write("\nCase #" + str(case_num) + ": " + line)
    case_num += 1
    first = False

main(sys.argv[-1])
