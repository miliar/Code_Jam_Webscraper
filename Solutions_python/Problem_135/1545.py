import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()
input = args.input
output = args.output
print "Reading input file", input

inputfile = open(input, "r")
outputfile = open(output, "w")

cases = int(inputfile.readline())
print "There are", cases, "test cases"

for x in range(0, cases):
    row1 = int(inputfile.readline())
    for y in range(0, 4):
        array = inputfile.readline().split()
        if y == row1 - 1:
            array1 = array

    row2 = int(inputfile.readline())
    for y in range(0, 4):
        array = inputfile.readline().split()
        if y == row2 - 1:
            array2 = array

    count = 0;        
    for item in array1:
        if item in array2:
            count += 1
            answer = item

    outputfile.write("Case #" + str(x + 1) + ": ")
    if count == 1:
        outputfile.write(answer)
    elif count == 0:
        outputfile.write("Volunteer cheated!")
    else:
        outputfile.write("Bad magician!")
    outputfile.write("\n")

inputfile.close()
outputfile.close()
